# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Userdata(models.Model):
    id = models.IntegerField(primary_key=True)
    ues_arm_field = models.TextField(db_column='UES (ARM)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ltts = models.TextField(db_column='LTTs', blank=True, null=True)  # Field name made lowercase.
    nomer_zajavki = models.IntegerField(db_column='Nomer zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_paketnoj_zajavki_mpz = models.FloatField(db_column='Nomer paketnoj zajavki MPZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vneshnij_istochnik_zajavki = models.FloatField(db_column='Vneshnij istochnik zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_zajavki_iz_vneshnego_istochnika = models.FloatField(db_column='Nomer zajavki iz vneshnego istochnika', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klient_field = models.TextField(db_column='Klient*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    inn = models.FloatField(db_column='INN', blank=True, null=True)  # Field name made lowercase.
    nls = models.FloatField(db_column='NLS', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    indeks = models.FloatField(db_column='Indeks', blank=True, null=True)  # Field name made lowercase.
    administrativnyj_rajon = models.TextField(db_column='Administrativnyj rajon', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    naselennyj_punkt = models.TextField(db_column='Naselennyj punkt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ulitsa = models.TextField(db_column='Ulitsa', blank=True, null=True)  # Field name made lowercase.
    dom = models.TextField(db_column='Dom', blank=True, null=True)  # Field name made lowercase.
    korpus = models.TextField(db_column='Korpus', blank=True, null=True)  # Field name made lowercase.
    kvartira = models.FloatField(db_column='Kvartira', blank=True, null=True)  # Field name made lowercase.
    adres_ustrojstva = models.TextField(db_column='Adres ustrojstva', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    data_vhoda_zajavki_v_status = models.TextField(db_column='Data vhoda zajavki v status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    zadacha_po_zajavke = models.TextField(db_column='Zadacha po zajavke', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    usluga = models.TextField(db_column='Usluga', blank=True, null=True)  # Field name made lowercase.
    kolichestvo_uslug = models.FloatField(db_column='Kolichestvo uslug', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dop_kanal_prodazh = models.FloatField(db_column='Dop. kanal prodazh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tabel_nyj_nomer = models.FloatField(db_column="Tabel'nyj nomer", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    naznachenie = models.TextField(db_column='Naznachenie', blank=True, null=True)  # Field name made lowercase.
    kanal_prodazh = models.TextField(db_column='Kanal prodazh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    segment = models.TextField(db_column='Segment', blank=True, null=True)  # Field name made lowercase.
    gts_sts = models.TextField(db_column='GTS/STS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_obraschenija = models.TextField(db_column='Data obraschenija', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_registratsii_zajavki = models.TextField(db_column='Data registratsii zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_registratsii_pod_zajavki = models.TextField(db_column='Data registratsii pod zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    reg_narjada_na_tvp = models.TextField(db_column='Reg. narjada na TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    zavershena_vruchnuju = models.TextField(db_column='Zavershena vruchnuju', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prichina_otkaza_klienta = models.TextField(db_column='Prichina otkaza klienta', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operator_zavershivshij_zajavku = models.FloatField(db_column='Operator zavershivshij zajavku', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_otklonenija_pod_zajavki = models.TextField(db_column='Data otklonenija pod zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    otklonena = models.TextField(db_column='Otklonena', blank=True, null=True)  # Field name made lowercase.
    tip_proverki_tvp = models.TextField(db_column='Tip proverki TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nalichie_tvp = models.TextField(db_column='Nalichie TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zavershenie_proverki_tvp = models.TextField(db_column='Zavershenie proverki TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dlit_proverki_tvp = models.TimeField(db_column='Dlit. proverki TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    norm_srok_proverki_tvp_chas_field = models.FloatField(db_column='Norm. srok proverki TVP (chas)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    prevyshenie_norm_sroka_proverki_tvp = models.TimeField(db_column='Prevyshenie norm. sroka proverki TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tehnologija = models.TextField(db_column='Tehnologija', blank=True, null=True)  # Field name made lowercase.
    sozdanie_dogovora = models.TextField(db_column='Sozdanie dogovora', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_registratsii_narjada_na_naznachenie_td = models.TextField(db_column='Data registratsii narjada na naznachenie TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    naznachenie_td = models.TextField(db_column='Naznachenie TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    tip_naznachenija_td = models.TextField(db_column='Tip Naznachenija TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dlit_naznachenija_td = models.TimeField(db_column='Dlit. naznachenija TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    norm_srok_naznachenija_td_chas_field = models.FloatField(db_column='Norm. srok naznachenija TD (chas)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    prevyshenie_norm_sroka_naznachenija_td = models.TextField(db_column='Prevyshenie norm. sroka naznachenija TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_soglasovanija_vremeni_vyezda_installjatora_pervaja_field = models.TextField(db_column='Data soglasovanija vremeni vyezda installjatora (pervaja)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    soglasovannaja_data_podkl_pervaja_field = models.TextField(db_column='Soglasovannaja data podkl. (pervaja)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    soglasovannaja_data_podkl_field = models.TextField(db_column='Soglasovannaja data podkl.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    zakrytie_narjada_na_podkl_field = models.TextField(db_column='Zakrytie narjada na podkl.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    norm_srok_podkl_dni_field = models.FloatField(db_column='Norm. srok podkl. (dni)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    prevyshenie_norm_sroka_podkl = models.TextField(db_column='Prevyshenie norm. sroka podkl', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prevyshenie_norm_sroka_podkl_dni_field = models.TextField(db_column='Prevyshenie norm. sroka podkl.  (dni)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    data_vypolnenija_agentom = models.TextField(db_column='Data vypolnenija agentom', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_peredachi_agentu = models.TextField(db_column='Data peredachi agentu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    instaljator = models.FloatField(db_column='Instaljator', blank=True, null=True)  # Field name made lowercase.
    agent_installjator = models.FloatField(db_column='Agent-installjator', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dlit_podkljuchenija_ot_reg_zajavki_v_is_field = models.TextField(db_column='Dlit. podkljuchenija (ot reg. zajavki v IS)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    dlit_podkljuchenija_ot_reg_zajavki_v_is_dni_field = models.TextField(db_column='Dlit. podkljuchenija (ot reg. zajavki v IS) (dni)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kol_vo_perenosov_srokov = models.IntegerField(db_column='Kol-vo perenosov srokov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    opisanie_prichiny_perenosa_srokov = models.TextField(db_column='Opisanie prichiny perenosa srokov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prichina_perenosa_srokov = models.TextField(db_column='Prichina perenosa srokov', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    annulirovan_pri_nalichii_tvp = models.TextField(db_column='Annulirovan pri nalichii TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vysvobozhdenie_nazn_td = models.TextField(db_column='Vysvobozhdenie nazn. TD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dlitel_nost_rezervir_td = models.TextField(db_column="Dlitel'nost' rezervir TD", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_nachala_dejstvija_dogovora_kurs = models.TextField(db_column='Data nachala dejstvija dogovora KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    sertifikat_ota = models.FloatField(db_column='Sertifikat OTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_ota_aktivirovan = models.FloatField(db_column='Sertifikat OTA aktivirovan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_ota_otklonen = models.FloatField(db_column='Sertifikat OTA otklonen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_internet = models.FloatField(db_column='Sertifikat Internet', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_internet_aktivirovan = models.FloatField(db_column='Sertifikat Internet aktivirovan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_internet_otklonen = models.FloatField(db_column='Sertifikat Internet otklonen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_iptv = models.FloatField(db_column='Sertifikat IPTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_iptv_aktivirovan = models.FloatField(db_column='Sertifikat IPTV aktivirovan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sertifikat_iptv_otklonen = models.FloatField(db_column='Sertifikat IPTV otklonen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kommentarij_tvp_ota = models.TextField(db_column='Kommentarij TVP OTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kommentarij_tvp_shpd = models.FloatField(db_column='Kommentarij TVP ShPD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    operator_zavodivshij_zajavku = models.FloatField(db_column='Operator zavodivshij zajavku', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kategorija_uslugi_pk = models.TextField(db_column='Kategorija uslugi PK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internet = models.TextField(db_column='Internet', blank=True, null=True)  # Field name made lowercase.
    ip_tv = models.TextField(db_column='IP-TV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ota = models.TextField(db_column='OTA', blank=True, null=True)  # Field name made lowercase.
    prjamoj_provod = models.TextField(db_column='Prjamoj provod', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fly = models.TextField(db_column='Fly', blank=True, null=True)  # Field name made lowercase.
    mvno = models.TextField(db_column='MVNO', blank=True, null=True)  # Field name made lowercase.
    kolichestvo_sim_kart = models.FloatField(db_column='Kolichestvo SIM-kart', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nachalo_zadachi_dop_to = models.TextField(db_column='Nachalo zadachi Dop. TO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    okonchanie_zadachi_dop_to = models.TextField(db_column='Okonchanie zadachi Dop. TO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    l_s_onima = models.FloatField(db_column='L/S Onima', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prichiny_otsutstvija_tvp = models.TextField(db_column='Prichiny otsutstvija TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prichiny_otsutstvija_tvp_iptv_field = models.FloatField(db_column='Prichiny otsutstvija TVP (IPTV)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    id_dogovor_kurs = models.FloatField(db_column='ID Dogovor KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_dogovora_kurs = models.FloatField(db_column='Nomer dogovora KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dlitel_nost_dop_to_dnej_field = models.TextField(db_column="Dlitel'nost' Dop. TO (dnej)", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    norm_srok_dop_to_dnej_field = models.FloatField(db_column='Norm.srok Dop. TO (dnej)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    narjad_kurs = models.FloatField(db_column='Narjad KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_zakrytija_narjada_kurs = models.TextField(db_column='Data zakrytija narjada KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    narjad_iptv_kurs = models.FloatField(db_column='Narjad IPTV KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_otkrytija_narjada_kurs = models.TextField(db_column='Data otkrytija narjada KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_zakrytija_narjada_iptv_kurs = models.TextField(db_column='Data zakrytija narjada IPTV KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    nomer_ota_shpd = models.TextField(db_column='Nomer OTA ShPD', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_otkrytija_narjada_iptv_kurs = models.TextField(db_column='Data otkrytija narjada IPTV KURS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    primechanie = models.FloatField(db_column='Primechanie', blank=True, null=True)  # Field name made lowercase.
    kontaktnyj_telefon = models.FloatField(db_column='Kontaktnyj telefon', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kontaktnoe_litso = models.FloatField(db_column='Kontaktnoe litso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fiz_litso = models.TextField(db_column='Fiz. litso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    jur_litso = models.TextField(db_column='Jur. litso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zakrytie_narjada_installjatorom = models.TextField(db_column='Zakrytie narjada installjatorom', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zadachi_vr_net_tvp = models.TextField(db_column='zadachi vr.net TVP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vip_klient = models.TextField(db_column='VIP-klient', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stoimost_tp_shpd_field = models.FloatField(db_column="Stoimost' TP (ShPD)", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stoimost_tp_iptv_field = models.FloatField(db_column="Stoimost' TP (IPTV)", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fio_sotrudnika_sozdavshego_dogovor = models.FloatField(db_column='FIO sotrudnika, sozdavshego dogovor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tarifnyj_plan_iptv = models.FloatField(db_column='Tarifnyj plan IPTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_karty_dostupa = models.FloatField(db_column='Nomer karty dostupa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_karty_dostupa_iptv = models.FloatField(db_column='Nomer karty dostupa IPTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tarifnyj_plan = models.FloatField(db_column='Tarifnyj plan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_privjazki_karty_v_onyma_shpd_field = models.TextField(db_column='Data privjazki karty v Onyma (ShPD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    data_privjazki_karty_v_onyma_iptv_field = models.TextField(db_column='Data privjazki karty v Onyma (IPTV)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    data_aktivatsii_uslugi_v_onyma_shpd_field = models.TextField(db_column='Data aktivatsii uslugi v Onyma (ShPD)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    data_aktivatsii_uslugi_v_onyma_iptv_field = models.TextField(db_column='Data aktivatsii uslugi v Onyma (IPTV)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    srok_zavershenija_ustanovki_wfm_field = models.TextField(db_column='Srok zavershenija ustanovki (WFM)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    uchastok_wfm_field = models.TextField(db_column='Uchastok (WFM)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sozdano_sotrudnikom_rrs = models.TextField(db_column='Sozdano sotrudnikom RRS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tspo = models.FloatField(db_column='TsPO', blank=True, null=True)  # Field name made lowercase.
    uslugi = models.FloatField(db_column='Uslugi', blank=True, null=True)  # Field name made lowercase.
    promo_aktsii = models.FloatField(db_column='Promo-aktsii', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tip_klienta_dlja_osv = models.TextField(db_column='Tip klienta dlja OSV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kanal_postuplenija_zajavki = models.TextField(db_column='Kanal postuplenija zajavki', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nomer_zakaza_cms = models.TextField(db_column='Nomer zakaza CMS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primechanie_pri_otkl_field = models.TextField(db_column='Primechanie pri otkl.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    germes_aptv = models.TextField(db_column='Germes APTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zajavka_arm_2_0 = models.TextField(db_column='Zajavka ARM 2.0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    klientskij_sus = models.FloatField(db_column='klientskij SUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stroitel_nyj_sus = models.FloatField(db_column="stroitel'nyj SUS", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    etap_sus = models.FloatField(db_column='Etap SUS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    migratsija_jul = models.TextField(db_column='Migratsija JuL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    proekt_sus_germes = models.FloatField(db_column='Proekt SUS Germes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ferrari = models.TextField(db_column='Ferrari', blank=True, null=True)  # Field name made lowercase.
    ferrari_bz = models.TextField(db_column='Ferrari BZ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_otpravki_na_aptv = models.TextField(db_column='Data otpravki na APTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_okonchanija_aptv_planiruemaja = models.TextField(db_column='Data okonchanija APTV planiruemaja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_okonchanija_aptv_fakticheskaja = models.TextField(db_column='Data okonchanija APTV fakticheskaja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dlitel_nost_etapa_aptv = models.TextField(db_column="Dlitel'nost' etapa APTV", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    data_otpravki_na_do = models.TextField(db_column='Data otpravki na DO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_okonchanija_do_planiruemaja = models.TextField(db_column='Data okonchanija DO planiruemaja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    data_okonchanija_do_fakticheskaja = models.TextField(db_column='Data okonchanija DO fakticheskaja', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    dlitel_nost_etapa_do = models.TextField(db_column="Dlitel'nost' etapa DO", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bronirovanie_cherez_germes = models.TextField(db_column='Bronirovanie cherez Germes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bronirovanie_cherez_argus_ruchnoe_field = models.TextField(db_column='Bronirovanie cherez Argus (ruchnoe)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    svetofor_germes_aptv = models.TextField(db_column='Svetofor Germes APTV', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gid_doma_orpon = models.FloatField(db_column='GID doma ORPON', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paketnoe_reshenie = models.TextField(db_column='Paketnoe reshenie', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    marker_paketa = models.TextField(db_column='Marker paketa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dop_usluga_1 = models.TextField(db_column='Dop.usluga 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dop_usluga_2 = models.FloatField(db_column='Dop.usluga 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dop_usluga_3 = models.FloatField(db_column='Dop.usluga 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zajavka_cherez_epk = models.TextField(db_column='Zajavka cherez EPK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    novyj_klient = models.TextField(db_column='Novyj klient', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Userdata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
