from utils.df_handle import *

def etl_to_postgres():
    # day_ago = 2
    datenow = datetime.now().strftime("%Y%m%d")
    # datenow_day_ago = ( datetime.now()-timedelta(day_ago) ).strftime("%Y%m%d")
    # param_1 = f"'{datenow_day_ago}'"
    # param_2 = f"'20210901'"
    param_3 = f"'{datenow}'"
    # param_4 = f"'20211109'"

    query = f"EXEC [pr_OM_RawdataSellOutPayroll_BI_v1] @Fromdate={param_3}, @Todate={param_3}"

    FINAL = get_ms_df(sql=query)

    if FINAL.shape[0] != 0 :

        FINAL.columns = cleancols(FINAL)

        FINAL.NgayGiaoHang.fillna(datetime(1900, 1, 1), inplace=True)

        FINAL['phanloaispcl'] = FINAL['MaSanPham'].map(
            df_to_dict(get_ps_df("select masanpham, phanloai from d_nhom_sp where nhomsp='SPCL'"))
        ).fillna('Khác')

        FINAL['nhomsp'] = FINAL['MaSanPham'].map(
            df_to_dict(get_ps_df("select masanpham, nhomsp from d_nhom_sp where nhomsp IN ('SPCL', 'SP MOI') "))
        ).fillna('Khác')

        FINAL['khuvucviettat'] = FINAL['TenKhuVuc'].map(
            df_to_dict(get_ps_df("select * from d_mkv_viet_tat"))
        )

        FINAL['chinhanh'] = FINAL['MaCongTyCN'].map(
            df_to_dict(get_ps_df("select * from d_chi_nhanh"))
        )

        FINAL['newhco'] = (FINAL['MaKenhPhu']+FINAL['MaPhanLoaiHCO']).map(
            df_to_dict(get_ps_df("SELECT concat(makenhphu, maphanloaihco) as concat, new_mahco FROM d_pl_hco"))
        )

        FINAL['phanam'] = FINAL['MaSanPham'].map(
            df_to_dict(get_ps_df("select masanpham, nhomsp from d_nhom_sp where nhomsp='PHA NAM'"))).fillna('Merap')

        FINAL['thang'] = FINAL['NgayChungTu'] + pd.offsets.Day() - pd.offsets.MonthBegin()

        FINAL['inserted_at'] = datetime.now()

        pk = ['macongtycn', 'ngaychungtu', 'sodondathang', 'masanpham', 'solo', 'lineref', 'soluong']

        execute_values_upsert(FINAL, 'f_sales', pk=pk)
    else:
        print('Not now')