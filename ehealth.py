from pintaros import model,view,fields,gui

class DataPasienModel(model.Model):
    _name = 'ehealth'
    _fid = 0x1234

    _columns = {
        'rekmed': fields.CharFields(20,'No Rekam Medis'),
        'kategori': fields.CharFields(50,'Kategori Pasien'),
        'asuransi': fields.CharFields(80,'No Asuransi'),
        'tanggaldaftar': fields.DateFields('Tanggal Daftar'),
        'nama' : fields.CharFields(50,'Nama'),
        'nama_kk': fields.CharFields(50,'Nama KK'),
        'hub_keluarga': fields.SelectFields(['Sendiri','Orang Tua','Kakek/Nenek','Anak','Saudara Kandung','Saudara Ayah','Saudara Ibu','Suami/Istri'],'drop','Hubungan Keluarga'),
        'kelamin' : fields.SelectFields(['Pria','Wanita'],'radio','Jenis Kelamin'),
        'alamat' : fields.CharFields(100,'Alamat'),
        'rt' : fields.NumberFields(100, 'RT'),
        'rw' : fields.NumberFields(100, 'RT'),
        'kelurahan' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kelurahan/Desa'),
        'kecamatan' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kecamatan'),
        'kota' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kota/Kabupaten'),
        'propinsi' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Propinsi'),
        'kodepos': fields.CharFields(5,'Kode Pos'),
        'kebangsaan' : fields.SelectFields(['WNI', 'WNA'], 'radio', 'Kebangsaan'),
        'tempatlahir' : fields.CharFields(20,'Tempat Lahir'),
        'tanggallahir' : fields.DateFields('Tanggal Lahir'),
        'goldarah' : fields.SelectFields(['A', 'B', 'AB', 'O', ''], 'radio', 'Golongan Darah'),
        'telepon' : fields.CharFields(16,'Telepon/HP'),
        'ktp' : fields.CharFields(16,'No KTP'),
        'status' : fields.SelectFields(['Menikah','Belum Menikah','Duda/Janda'],'radio','Status Pernihakan'),
        'agama' : fields.SelectFields(['Islam','Kristen','Protestan','Hindu','Budha','Lainnya'],'drop','Agama'),
        'pekerjaan' : fields.SelectFields(['PNS','TNI/POLRI','Pensiunan','Swasta','Pedagang','Nelayan','Petani','Pekerja lepas / Wiraswasta','Ibu Rumah Tangga', 'Pelajar', 'Mahasiswa', 'Dibawah umur', 'Tidak bekerja'],'drop','Pekerjaan'),
        'pendidikan' : fields.SelectFields(['SD','SMP','SMA','D1','D2','D3','S1/D4','S2','S3'],'drop','Pendidikan'),
        'kontak_nama' : fields.CharFields(50,'Nama'),
        'kontak_hubungan' : fields.SelectFields(['Orang Tua','Kakek/Nenek','Anak','Saudara Kandung','Saudara Ayah','Saudara Ibu','Suami/Istri'],'drop','Hubungan Keluarga'),
        'kontak_alamat' : fields.CharFields(100, 'Alamat'),
        'kontak_rt' : fields.NumberFields(100, 'RT'),
        'kontak_rw' : fields.NumberFields(100, 'RT'),
        'kontak_kelurahan' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kelurahan/Desa'),
        'kontak_kecamatan' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kecamatan'),
        'kontak_kota' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Kota/Kabupaten'),
        'kontak_propinsi' : fields.SelectFields(['satu', 'dua', 'tiga'], 'drop', 'Propinsi'),
        'kontak_kodepos': fields.CharFields(5,'Kode Pos'),
        'kontak_telepon' : fields.CharFields(16,'Telepon/HP'),        
    }

class DataPasienView(view.View):
    _model = 'ehealth'
    _columns = ['nama',
                'kelamin',
                'alamat',
                'rt',
                'rw',
                'kelurahan',
                'kecamatan',
                'kota',
                'propinsi',
                'kebangsaan',
                'tempatlahir',
                'tanggallahir',
                'goldarah',
                'telepon',
                'ktp',
                'status',
                'agama',
                'pekerjaan',
                'pendidikan',
    ]

app_models = [DataPasienModel]
app_view = [DataPasienView]

app = gui.Gui(app_models,app_view)
app.run()