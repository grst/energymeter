"""Not used by this project, but nice reference of the registers and their data types"""

from modbus import Modbus
from Register import S16, S32, STR32, U16, U32, U64


def add_tripower_register(wr: Modbus):
    wr.add_register(U32(30051, "Nameplate.MainModel", "Geräteklasse"))
    wr.add_register(U32(30053, "Nameplate.Model", "Gerätetyp"))
    wr.add_register(U32(30055, "Nameplate.Vendor", "Hersteller"))
    wr.add_register(U32(30057, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(30059, "Nameplate.PkgRev", "Softwarepaket"))
    wr.add_register(U32(30199, "Operation.RmgTms", "Wartezeit bis Einspeisung"))
    wr.add_register(U32(30201, "Operation.Health", "Zustand"))
    wr.add_register(U32(30203, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(U32(30205, "Operation.HealthStt.Wrn", "Nennleistung im Zustand Warnung"))
    wr.add_register(U32(30207, "Operation.HealthStt.Alm", "Nennleistung im Zustand Fehler"))
    wr.add_register(U32(30211, "Operation.Evt.Prio", "Empfohlene Aktion"))
    wr.add_register(U32(30213, "Operation.Evt.Msg", "Meldung"))
    wr.add_register(U32(30215, "Operation.Evt.Dsc", "Fehlerbehebungsmaßnahme"))
    wr.add_register(U32(30217, "Operation.GriSwStt", "Netzrelais/-schütz"))
    wr.add_register(U32(30219, "Operation.DrtStt", "Leistungsreduzierung"))
    wr.add_register(U32(30225, "Isolation.LeakRis", "Isolationswiderstand"))
    wr.add_register(U32(30231, "Inverter.WLim", "Maximale Gerätewirkleistung"))
    wr.add_register(U32(30233, "Inverter.WMax", "Eingestellte Wirkleistungsgrenze"))
    wr.add_register(U32(30247, "Operation.Evt.EvtNo", "Aktuelle Ereignisnummer für Hersteller"))
    wr.add_register(U64(30513, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U64(30521, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U64(30525, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U32(30529, "Metering.TotWhOut", "Gesamtertrag Wh"))
    wr.add_register(U32(30531, "Metering.TotWhOut", "Gesamtertrag kWh"))
    wr.add_register(U32(30533, "Metering.TotWhOut", "Gesamtertrag MWh"))
    wr.add_register(U32(30541, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U32(30543, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U32(30559, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U32(30561, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U32(30563, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U32(30581, "Metering.GridMs.TotWhIn", "Zählerstand Bezugszähler"))
    wr.add_register(U32(30583, "Metering.GridMs.TotWhOut", "Zählerstand Einspeisezähler"))
    wr.add_register(U32(30599, "Operation.GriSwCnt", "Anzahl Netzzuschaltungen"))
    wr.add_register(S32(30769, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(30771, "DcMs.Vol", "DC Spannung Eingang"))
    wr.add_register(S32(30773, "DcMs.Watt", "DC Leistung Eingang"))
    wr.add_register(S32(30775, "GridMs.TotW", "Leistung"))
    wr.add_register(S32(30777, "GridMs.W.phsA", "Leistung L1"))
    wr.add_register(S32(30779, "GridMs.W.phsB", "Leistung L2"))
    wr.add_register(S32(30781, "GridMs.W.phsC", "Leistung L3"))
    wr.add_register(U32(30783, "GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(30785, "GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(30787, "GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(30789, "GridMs.PhV.phsA2B", "Netzspannung Phase L1 gegen L2"))
    wr.add_register(U32(30791, "GridMs.PhV.phsB2C", "Netzspannung Phase L2 gegen L3"))
    wr.add_register(U32(30793, "GridMs.PhV.phsC2A", "Netzspannung Phase L3 gegen L1"))
    wr.add_register(U32(30795, "GridMs.TotA", "Netzstrom"))
    wr.add_register(U32(30803, "GridMs.Hz", "Netzfrequenz"))
    wr.add_register(S32(30805, "GridMs.TotVAr", "Blindleistung"))
    wr.add_register(S32(30807, "GridMs.VAr.phsA", "Blindleistung L1"))
    wr.add_register(S32(30809, "GridMs.VAr.phsB", "Blindleistung L2"))
    wr.add_register(S32(30811, "GridMs.VAr.phsC", "Blindleistung L3"))
    wr.add_register(S32(30813, "GridMs.TotVA", "Scheinleistung"))
    wr.add_register(S32(30815, "GridMs.VA.phsA", "Scheinleistung L1"))
    wr.add_register(S32(30817, "GridMs.VA.phsB", "Scheinleistung L2"))
    wr.add_register(S32(30819, "GridMs.VA.phsC", "Scheinleistung L3"))
    wr.add_register(
        U32(
            30825,
            "Inverter.VArModCfg.VArMod",
            "Betriebsart der statischen Spannungshaltung, Konfiguration der statischen Spannungshaltung",
        )
    )
    wr.add_register(S32(30829, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Blindleistungssollwert in %"))
    wr.add_register(
        S32(
            30831, "Inverter.VArModCfg.PFCnstCfg.PF", "Sollwert des cos Phi, Konfiguration des cos Phi, direkte Vorgabe"
        )
    )
    wr.add_register(
        U32(
            30833,
            "Inverter.VArModCfg.PFCnstCfg.PFExt",
            "Erregungsart des cos Phi, Konfiguration des cos Phi, direkte Vorgabe",
        )
    )
    wr.add_register(U32(30835, "Inverter.WModCfg.WMod", "Betriebsart des Einspeisemanagements"))
    wr.add_register(U32(30837, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(U32(30839, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(S32(30865, "Metering.GridMs.TotWIn", "Leistung Bezug"))
    wr.add_register(S32(30867, "Metering.GridMs.TotWOut", "Leistung Einspeisung"))
    wr.add_register(U32(30875, "MltFncSw.Stt", "Status des Multifunktionsrelais"))
    wr.add_register(U32(30881, "Operation.PvGriConn", "Netzanbindung der Anlage"))
    wr.add_register(U32(30925, "Spdwr.ComSocA.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM A"))
    wr.add_register(U32(30927, "Spdwr.ComSocA.DpxMode", "Duplexmodus von SMACOM A"))
    wr.add_register(U32(30929, "Spdwr.ComSocA.Stt", "Speedwire-Verbindungsstatus von SMACOM A"))
    wr.add_register(U32(30931, "Spdwr.ComSocB.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM B"))
    wr.add_register(U32(30933, "Spdwr.ComSocB.DpxMode", "Duplexmodus von SMACOM B"))
    wr.add_register(U32(30935, "Spdwr.ComSocB.Stt", "Speedwire-Verbindungsstatus von SMACOM B"))
    wr.add_register(U32(30949, "GridMs.TotPFPrc", "Verschiebungsfaktor"))
    wr.add_register(S32(30953, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(S32(30957, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(30959, "DcMs.Vol", "DC Spannung Eingang"))
    wr.add_register(S32(30961, "DcMs.Watt", "DC Leistung Eingang"))
    wr.add_register(S32(30975, "Inverter.DclVol", "Zwischenkreisspannung"))
    wr.add_register(S32(30977, "GridMs.A.phsA", "Netzstrom Phase L1"))
    wr.add_register(S32(30979, "GridMs.A.phsB", "Netzstrom Phase L2"))
    wr.add_register(S32(30981, "GridMs.A.phsC", "Netzstrom Phase L3"))
    wr.add_register(STR32(31017, "Spdwr.ActlIp", "-"))
    wr.add_register(STR32(31025, "Spdwr.ActlSnetMsk", "-"))
    wr.add_register(STR32(31033, "Spdwr.ActlGwIp", "-"))
    wr.add_register(STR32(31041, "Spdwr.ActlDnsSrvIp", "-"))
    wr.add_register(U32(31061, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(U32(31085, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(S32(31159, "Operation.Dmd.VArCtl", "Aktuelle Vorgabe Blindleistung Q"))
    wr.add_register(S32(31221, "GridMs.TotPFEEI", "EEI-Verschiebungsfaktor"))
    wr.add_register(S32(31247, "Isolation.FltA", "Fehlerstrom"))
    wr.add_register(U32(31253, "Metering.GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(31255, "Metering.GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(31257, "Metering.GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(31259, "Metering.GridMs.W.phsA", "Leistung Netzeinspeisung L1"))
    wr.add_register(U32(31261, "Metering.GridMs.W.phsB", "Leistung Netzeinspeisung L2"))
    wr.add_register(U32(31263, "Metering.GridMs.W.phsC", "Leistung Netzeinspeisung L3"))
    wr.add_register(U32(31265, "Metering.GridMs.WIn.phsA", "Leistung Netzbezug Phase L1"))
    wr.add_register(U32(31267, "Metering.GridMs.WIn.phsB", "Leistung Netzbezug Phase L2"))
    wr.add_register(U32(31269, "Metering.GridMs.WIn.phsC", "Leistung Netzbezug Phase L3"))
    wr.add_register(S32(31271, "Metering.GridMs.VAr.phsA", "Blindleistung Netzeinspeisung Phase L1"))
    wr.add_register(S32(31273, "Metering.GridMs.VAr.phsB", "Blindleistung Netzeinspeisung Phase L2"))
    wr.add_register(S32(31275, "Metering.GridMs.VAr.phsC", "Blindleistung Netzeinspeisung Phase L3"))
    wr.add_register(S32(31277, "Metering.GridMs.TotVAr", "Blindleistung Netzeinspeisung"))
    wr.add_register(U32(31405, "Operation.Dmd.WCtl", "Aktuelle Vorgabe Wirkleistungsbegrenzung P"))
    wr.add_register(U32(31407, "Operation.Dmd.PFCtl", "Aktuelle Vorgabe cos Phi"))
    wr.add_register(U32(31409, "Operation.Dmd.PFExtCtl", "Aktuelle Vorgabe Erregungsart cos Phi"))
    wr.add_register(S32(31411, "Operation.Dmd.VArCtl", "Aktuelle Vorgabe Blindleistung Q"))
    wr.add_register(S32(31793, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(31795, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(34113, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(S32(34609, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34611, "Env.TmpValMax", "Höchste gemessene Außentemperatur"))
    wr.add_register(U32(34615, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(S32(34621, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(U32(34623, "Env.ExInsol", "Einstrahlung auf externen Sensor"))
    wr.add_register(S32(34625, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34627, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34629, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(S32(34631, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(U32(34633, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34635, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34669, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(U64(35377, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U64(35381, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U64(35385, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U32(40003, "DtTm.TmZn", "Zeitzone"))
    wr.add_register(U32(40005, "DtTm.DlSvIsOn", "Automatische Sommer-/Winterzeitumstellung eingeschaltet"))
    wr.add_register(U32(40009, "Operation.OpMod", "Betriebszustand"))
    wr.add_register(U32(40013, "CntrySettings.Lang", "Sprache der Oberfläche"))
    wr.add_register(
        S16(40015, "Inverter.VArModCfg.VArCtlComCfg.VArNom", "Normierte Blindleistungsvorgabe durch Anlagensteuerung")
    )
    wr.add_register(
        S16(40016, "Inverter.WModCfg.WCtlComCfg.WNom", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(U32(40018, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(
        S16(
            40022,
            "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc",
            "Normierte Blindleistungsbegrenzung durch Anlagensteuerung",
        )
    )
    wr.add_register(
        S16(40023, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(U16(40024, "Inverter.VArModCfg.PFCtlComCfg.PF", "Verschiebungsfaktor durch Anlagensteuerung"))
    wr.add_register(U32(40025, "Inverter.VArModCfg.PFCtlComCfg.PFExt", "Erregungsart durch Anlagensteuerung"))
    wr.add_register(U32(40029, "Operation.OpStt", "Betriebsstatus"))
    wr.add_register(U32(40063, "Nameplate.CmpMain.SwRev", "Firmware-Version des Hauptprozessors"))
    wr.add_register(U32(40067, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(40077, "Sys.DevRstr", "Geräteneustart auslösen"))
    wr.add_register(U32(40095, "GridGuard.Cntry.VolCtl.Max", "Spannungsüberwachung obere Maximalschwelle"))
    wr.add_register(U32(40109, "GridGuard.Cntry", "Eingestellte Ländernorm"))
    wr.add_register(U32(40133, "GridGuard.Cntry.VRtg", "Netz-Nennspannung"))
    wr.add_register(U32(40135, "GridGuard.Cntry.HzRtg", "Nennfrequenz"))
    wr.add_register(S32(40149, "Inverter.WModCfg.WCtlComCfg.WSpt", "Wirkleistungsvorgabe"))
    wr.add_register(
        U32(40151, "Inverter.WModCfg.WCtlComCfg.WCtlComAct", "Wirk- und Blindleistungsregelung über Kommunikation")
    )
    wr.add_register(U32(40157, "Spdwr.AutoCfgIsOn", "Automatische Speedwire-Konfiguration eingeschaltet"))
    wr.add_register(STR32(40159, "Spdwr.Ip", "-"))
    wr.add_register(STR32(40167, "Spdwr.SnetMsk", "-"))
    wr.add_register(STR32(40175, "Spdwr.GwIp", "-"))
    wr.add_register(U32(40185, "Inverter.VALim", "Maximale Gerätescheinleistung"))
    wr.add_register(U32(40195, "Inverter.VAMax", "Eingestellte Scheinleistungsgrenze"))
    wr.add_register(
        U32(
            40200,
            "Inverter.VArModCfg.VArMod",
            "Betriebsart der statischen Spannungshaltung, Konfiguration der statischen Spannungshaltung",
        )
    )
    wr.add_register(S32(40204, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Blindleistungssollwert in %"))
    wr.add_register(
        S32(
            40206, "Inverter.VArModCfg.PFCnstCfg.PF", "Sollwert des cos Phi, Konfiguration des cos Phi, direkte Vorgabe"
        )
    )
    wr.add_register(
        U32(
            40208,
            "Inverter.VArModCfg.PFCnstCfg.PFExt",
            "Erregungsart des cos Phi, Konfiguration des cos Phi, direkte Vorgabe",
        )
    )
    wr.add_register(U32(40210, "Inverter.WModCfg.WMod", "Betriebsart des Einspeisemanagements"))
    wr.add_register(U32(40212, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(U32(40214, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(
        U32(40216, "Inverter.WCtlHzModCfg.WCtlHzMod", "Betriebsart der Wirkleistungsreduktion bei Überfrequenz P(f)")
    )
    wr.add_register(
        U32(
            40218,
            "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStr",
            "Abstand der Startfrequenz zur Netzfrequenz, Konfiguration des linearen Gradienten der Momentanleistung",
        )
    )
    wr.add_register(
        U32(
            40220,
            "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStop",
            "Abstand der Rücksetzfrequenz zur Netzfrequenz, Konfiguration des linearen Gradienten der Momentanleistung",
        )
    )
    wr.add_register(
        U32(
            40222,
            "Inverter.VArModCfg.PFCtlWCfg.PFStr",
            "cos Phi des Startpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(
        U32(
            40224,
            "Inverter.VArModCfg.PFCtlWCfg.PFExtStr",
            "Erregungsart des Startpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(
        U32(
            40226,
            "Inverter.VArModCfg.PFCtlWCfg.PFStop",
            "cos Phi des Endpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(
        U32(
            40228,
            "Inverter.VArModCfg.PFCtlWCfg.PFExtStop",
            "Erregungsart des Endpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(
        U32(
            40230,
            "Inverter.VArModCfg.PFCtlWCfg.WNomStr",
            "Wirkleistung des Startpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(
        U32(
            40232,
            "Inverter.VArModCfg.PFCtlWCfg.WNomStop",
            "Wirkleistung des Endpunktes, Konfiguration der cos Phi(P)-Kennlinie",
        )
    )
    wr.add_register(U32(40234, "Inverter.WGra", "Wirkleistungsgradient"))
    wr.add_register(
        U32(
            40238,
            "Inverter.WCtlHzModCfg.WCtlHzCfg.WGra",
            "Wirkleistungsgradient, Konfiguration des linearen Gradienten der Momentanleistung",
        )
    )
    wr.add_register(
        U32(
            40240,
            "Inverter.WCtlHzModCfg.WCtlHzCfg.HystEna",
            "Aktivierung der Schleppzeigerfunktion, Konfiguration des linearen Gradienten der Momentanleistung",
        )
    )
    wr.add_register(
        U32(
            40242,
            "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStopWGra",
            "Wirkleistungsgradient nach Rücksetzfrequenz, Konfiguration des linearen Gradienten der Momentanleistung",
        )
    )
    wr.add_register(
        U32(
            40244,
            "Inverter.DGSModCfg.DGSFlCfg.ArGraMod",
            "Blindstromstatik, Konfiguration der vollständigen dynamischen Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40246,
            "Inverter.DGSModCfg.DGSFlCfg.ArGraSag",
            "Gradient K der Blindstromstatik für Unterpannung bei dynamischer Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40248,
            "Inverter.DGSModCfg.DGSFlCfg.ArGraSwell",
            "Gradient K der Blindstromstatik für Überpannung bei dynamischer Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40250,
            "Inverter.DGSModCfg.DGSMod",
            "Betriebsart der dynamischen Netzstützung, Konfiguration der dynamischen Netzstützung",
        )
    )
    wr.add_register(
        S32(
            40252,
            "Inverter.DGSModCfg.DGSFlCfg.DbVolNomMin",
            "Untergrenze Spannungstotband, Konfiguration der vollständigen dynamischen Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40254,
            "Inverter.DGSModCfg.DGSFlCfg.DbVolNomMax",
            "Obergrenze Spannungstotband, Konfiguration der vollständigen dynamischen Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40256,
            "Inverter.DGSModCfg.PwrCirInopVolNom",
            "PWM-Sperrspannung, Konfiguration der dynamischen Netzstützung",
        )
    )
    wr.add_register(
        U32(
            40258,
            "Inverter.DGSModCfg.PwrCirInopTms",
            "PWM-Sperrverzögerung, Konfiguration der dynamischen Netzstützung",
        )
    )
    wr.add_register(
        U32(40262, "Inverter.UtilCrvCfg.Crv0.NumPt", "Kennlinie, Anzahl der zu verwendenden Punkte der Kennlinie")
    )
    wr.add_register(
        U32(40264, "Inverter.UtilCrvCfg.Crv0.NumPt", "Kennlinie, Anzahl der zu verwendenden Punkte der Kennlinie")
    )
    wr.add_register(
        U32(40266, "Inverter.UtilCrvCfg.Crv0.NumPt", "Kennlinie, Anzahl der zu verwendenden Punkte der Kennlinie")
    )
    wr.add_register(S32(40282, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40284, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40286, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40288, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40290, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40292, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40294, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40296, "Inverter.UtilCrvCfg.CrvPt1.XVal", "X-Werte der Kennlinie 1"))
    wr.add_register(S32(40306, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40308, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40310, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40312, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40314, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40316, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40318, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40320, "Inverter.UtilCrvCfg.CrvPt1.YVal", "Y-Werte der Kennlinie 1"))
    wr.add_register(S32(40330, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40332, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40334, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40336, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40338, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40340, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40342, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40344, "Inverter.UtilCrvCfg.CrvPt2.XVal", "X-Werte der Kennlinie 2"))
    wr.add_register(S32(40354, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40356, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40358, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40360, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40362, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40364, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40366, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40368, "Inverter.UtilCrvCfg.CrvPt2.YVal", "Y-Werte der Kennlinie 2"))
    wr.add_register(S32(40378, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40380, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40382, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40384, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40386, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40388, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40390, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40392, "Inverter.UtilCrvCfg.CrvPt3.XVal", "X-Werte der Kennlinie 3"))
    wr.add_register(S32(40402, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40404, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40406, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40408, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40410, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40412, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40414, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(S32(40416, "Inverter.UtilCrvCfg.CrvPt3.YVal", "Y-Werte der Kennlinie 3"))
    wr.add_register(U32(40428, "GridGuard.Cntry.FrqCtl.hhLim", "Frequenzüberwachung mittlere Maximalschwelle"))
    wr.add_register(
        U32(40430, "GridGuard.Cntry.FrqCtl.hhLimTmms", "Frequenzüberwachung mittlere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40432, "GridGuard.Cntry.FrqCtl.hLim", "Frequenzüberwachung untere Maximalschwelle"))
    wr.add_register(
        U32(40434, "GridGuard.Cntry.FrqCtl.hLimTmms", "Frequenzüberwachung untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40436, "GridGuard.Cntry.FrqCtl.lLim", "Frequenzüberwachung obere Minimalschwelle"))
    wr.add_register(
        U32(40438, "GridGuard.Cntry.FrqCtl.lLimTmms", "Frequenzüberwachung obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(40440, "GridGuard.Cntry.FrqCtl.llLim", "Frequenzüberwachung mittlere Minimalschwelle"))
    wr.add_register(
        U32(40442, "GridGuard.Cntry.FrqCtl.llLimTmms", "Frequenzüberwachung mittlere Minimalschwelle Auslösezeit")
    )
    wr.add_register(
        U32(40446, "GridGuard.Cntry.VolCtl.MaxTmms", "Spannungsüberwachung obere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40448, "GridGuard.Cntry.VolCtl.hhLim", "Spannungsüberwachung mittlere Maximalschwelle"))
    wr.add_register(
        U32(40450, "GridGuard.Cntry.VolCtl.hhLimTmms", "Spannungsüberwachung mittlere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40452, "GridGuard.Cntry.VolCtl.hLim", "Spannungsüberwachung untere Maximalschwelle"))
    wr.add_register(
        U32(40456, "GridGuard.Cntry.VolCtl.hLimTmms", "Spannungsüberwachung untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40458, "GridGuard.Cntry.VolCtl.lLim", "Spannungsüberwachung obere Minimalschwelle"))
    wr.add_register(
        U32(40462, "GridGuard.Cntry.VolCtl.lLimTmms", "Spannungsüberwachung obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(40464, "GridGuard.Cntry.VolCtl.llLim", "Spannungsüberwachung mittlere Minimalschwelle"))
    wr.add_register(
        U32(40466, "GridGuard.Cntry.VolCtl.llLimTmms", "Spannungsüberwachung mittlere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(40472, "Inverter.PlntCtl.VRef", "Referenzspannung"))
    wr.add_register(S32(40474, "Inverter.PlntCtl.VRefOfs", "Referenzkorrekturspannung"))
    wr.add_register(U32(40480, "Nameplate.ARtg", "Nennstrom über alle Phasen"))
    wr.add_register(U32(40482, "Inverter.VArGra", "Blindleistungsgradient"))
    wr.add_register(U32(40484, "Inverter.WGraEna", "Aktivierung des Wirkleistungsgradienten"))
    wr.add_register(
        U32(
            40490,
            "Inverter.VArModCfg.VArCtlVolCfg.VArGraNom",
            "Blindleistungsgradient, Konfiguration der Blindleistungs-/Spannungskennlinie Q(U)",
        )
    )
    wr.add_register(STR32(40497, "Nameplate.MacId", "-"))
    wr.add_register(STR32(40513, "Spdwr.DnsSrvIp", "-"))
    wr.add_register(U32(40575, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(U32(40577, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(STR32(40631, "Nameplate.Location", "-"))
    wr.add_register(U32(40647, "Upd.AutoUpdIsOn", "Automatische Updates eingeschaltet"))
    wr.add_register(U32(40789, "Nameplate.ComRev", "Kommunikationsversion"))
    wr.add_register(U32(40791, "Inverter.PlntCtl.IntvTmsMax", "Timeout für Kommunikationsfehlermeldung"))
    wr.add_register(
        U32(
            40855,
            "Inverter.UtilCrvCfg.Crv0.RmpDec",
            "Kennlinie, Absenkungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(
            40857,
            "Inverter.UtilCrvCfg.Crv0.RmpDec",
            "Kennlinie, Absenkungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(
            40859,
            "Inverter.UtilCrvCfg.Crv0.RmpDec",
            "Kennlinie, Absenkungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(
            40875,
            "Inverter.UtilCrvCfg.Crv0.RmpInc",
            "Kennlinie, Steigerungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(
            40877,
            "Inverter.UtilCrvCfg.Crv0.RmpInc",
            "Kennlinie, Steigerungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(
            40879,
            "Inverter.UtilCrvCfg.Crv0.RmpInc",
            "Kennlinie, Steigerungsrampe für Erreichung des Kennlinienarbeitspunktes",
        )
    )
    wr.add_register(
        U32(40895, "Inverter.UtilCrvCfg.Crv0.CrvTms", "Kennlinie, Einstellzeit des Kennlinienarbeitspunktes")
    )
    wr.add_register(
        U32(40897, "Inverter.UtilCrvCfg.Crv0.CrvTms", "Kennlinie, Einstellzeit des Kennlinienarbeitspunktes")
    )
    wr.add_register(
        U32(40899, "Inverter.UtilCrvCfg.Crv0.CrvTms", "Kennlinie, Einstellzeit des Kennlinienarbeitspunktes")
    )
    wr.add_register(U32(40915, "Inverter.WMax", "Eingestellte Wirkleistungsgrenze"))
    wr.add_register(
        U32(40917, "Inverter.UtilCrvCfg.CrvModCfg.CrvNum", "Kennliniennummer, Konfiguration des Kennlinienmodus")
    )
    wr.add_register(
        U32(40919, "Inverter.UtilCrvCfg.CrvModCfg.CrvNum", "Kennliniennummer, Konfiguration des Kennlinienmodus")
    )
    wr.add_register(
        U32(40921, "Inverter.UtilCrvCfg.CrvModCfg.CrvNum", "Kennliniennummer, Konfiguration des Kennlinienmodus")
    )
    wr.add_register(
        U32(
            40937,
            "Inverter.UtilCrvCfg.CrvModCfg.CrvEna",
            "Aktivierung der Kennlinie, Konfiguration des Kennlinienmodus",
        )
    )
    wr.add_register(
        U32(
            40939,
            "Inverter.UtilCrvCfg.CrvModCfg.CrvEna",
            "Aktivierung der Kennlinie, Konfiguration des Kennlinienmodus",
        )
    )
    wr.add_register(
        U32(
            40941,
            "Inverter.UtilCrvCfg.CrvModCfg.CrvEna",
            "Aktivierung der Kennlinie, Konfiguration des Kennlinienmodus",
        )
    )
    wr.add_register(U32(40957, "Inverter.UtilCrvCfg.Crv0.XRef", "Kennlinie X-Achsen Referenz"))
    wr.add_register(U32(40959, "Inverter.UtilCrvCfg.Crv0.XRef", "Kennlinie X-Achsen Referenz"))
    wr.add_register(U32(40961, "Inverter.UtilCrvCfg.Crv0.XRef", "Kennlinie X-Achsen Referenz"))
    wr.add_register(U32(40977, "Inverter.UtilCrvCfg.Crv0.YRef", "Kennlinie Y-Achsen Referenz"))
    wr.add_register(U32(40979, "Inverter.UtilCrvCfg.Crv0.YRef", "Kennlinie Y-Achsen Referenz"))
    wr.add_register(U32(40981, "Inverter.UtilCrvCfg.Crv0.YRef", "Kennlinie Y-Achsen Referenz"))
    wr.add_register(
        U32(40997, "Inverter.DGSModCfg.HystVolNom", "Hysteresespannung, Konfiguration der dynamischen Netzstützung")
    )
    wr.add_register(S32(40999, "Inverter.VArModCfg.PFCtlComCfg.PFEEI", "Sollwert cos(Phi) gemäß EEI-Konvention"))
    wr.add_register(U32(41121, "GridGuard.CntrySet", "Setze Ländernorm"))
    wr.add_register(U32(41123, "GridGuard.Cntry.VolCtl.ReconMin", "Min. Spannung zur Wiederzuschaltung"))
    wr.add_register(U32(41125, "GridGuard.Cntry.VolCtl.ReconMax", "Max. Spannung zur Wiederzuschaltung"))
    wr.add_register(U32(41127, "GridGuard.Cntry.FrqCtl.ReconMin", "Untere Frequenz für Wiederzuschaltung"))
    wr.add_register(U32(41129, "GridGuard.Cntry.FrqCtl.ReconMax", "Obere Frequenz für Wiederzuschaltung"))
    wr.add_register(U32(41131, "DcCfg.StrVol", "minimale Spannung Eingang "))
    wr.add_register(U32(41133, "DcCfg.StrVol", "minimale Spannung Eingang "))
    wr.add_register(U32(41155, "DcCfg.StrTms", "Startverzögerung Eingang "))
    wr.add_register(U32(41157, "DcCfg.StrTms", "Startverzögerung Eingang "))
    wr.add_register(U32(41169, "GridGuard.Cntry.LeakRisMin", "Minimaler Isolationswiderstand"))
    wr.add_register(U32(41171, "Metering.TotkWhOutSet", "Setze Gesamtertrag"))
    wr.add_register(U32(41173, "Metering.TotOpTmhSet", "Setze Gesamte Betriebszeit am Netzanschlusspunkt"))
    wr.add_register(
        U32(41187, "Inverter.CtlComCfg.CtlMsSrc", "Quelle der Referenzmessung zur Blind-/Wirkleistungsregelung")
    )
    wr.add_register(
        U32(41193, "Inverter.CtlComCfg.WCtlCom.CtlComMssMod", "Betriebsart für ausbleibende Wirkleistungsbegrenzung")
    )
    wr.add_register(U32(41195, "Inverter.CtlComCfg.WCtlCom.TmsOut", "Timeout für ausbleibende Wirkleistungsbegrenzung"))
    wr.add_register(
        U32(
            41197,
            "Inverter.CtlComCfg.WCtlCom.FlbWNom",
            "Fallback Wirkleistungsbegrenzung P in % von WMax für ausbleibende Wirkleistungsbegrenzung",
        )
    )
    wr.add_register(U32(41199, "PCC.WMaxNom", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(U32(41203, "Plnt.DcWRtg", "Anlagen-Nennleistung"))
    wr.add_register(S32(41215, "Inverter.WModCfg.WCtlComCfg.FlbWSpt", "Fallback Leistung für Betriebsart WCtlCom"))
    wr.add_register(U32(41217, "PCC.WMax", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(
        U32(41219, "Inverter.CtlComCfg.VArCtlCom.CtlComMssMod", "Betriebsart für ausbleibende Blindleistungsregelung")
    )
    wr.add_register(
        U32(41221, "Inverter.CtlComCfg.VArCtlCom.TmsOut", "Timeout für ausbleibende Blindleistungsregelung")
    )
    wr.add_register(
        S32(
            41223,
            "Inverter.CtlComCfg.VArCtlCom.FlbVArNom",
            "Fallback Blindleistung Q in % von WMax für ausbleibende Blindleistungsregelung",
        )
    )
    wr.add_register(
        U32(41225, "Inverter.CtlComCfg.PFCtlCom.CtlComMssMod", "Betriebsart für ausbleibende cos Phi-Vorgabe")
    )
    wr.add_register(U32(41227, "Inverter.CtlComCfg.PFCtlCom.TmsOut", "Timeout für ausbleibende cos Phi-Vorgabe"))
    wr.add_register(
        S32(41229, "Inverter.CtlComCfg.PFCtlCom.FlbPF", "Fallback cos Phi für ausbleibende cos Phi-Vorgabe")
    )
    wr.add_register(U32(41253, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(
        S16(41255, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(
        S16(
            41256,
            "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc",
            "Normierte Blindleistungsbegrenzung durch Anlagensteuerung",
        )
    )
    wr.add_register(S32(41257, "Inverter.VArModCfg.PFCtlComCfg.PFEEI", "Sollwert cos(Phi) gemäß EEI-Konvention"))


# Modbus registers for SB3.0-1AV-41 / SB3.6-1AV-41 / SB4.0-1AV-41 / SB5.0-1AV-41 / SB6.0-1AV-41 (V12)


def add_sbxx_1av_41_register(wr: Modbus):
    wr.add_register(STR32(40497, "Nameplate.MacId", "-"))
    wr.add_register(U32(30059, "Nameplate.PkgRev", "Softwarepaket"))
    wr.add_register(U32(30559, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U64(35377, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U32(30561, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U64(35381, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U32(30563, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U64(35385, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U32(30215, "Operation.Evt.Dsc", "Fehlerbehebungsmaßnahme"))
    wr.add_register(U32(30247, "Operation.Evt.EvtNo", "Aktuelle Ereignisnummer für Hersteller"))
    wr.add_register(U32(30213, "Operation.Evt.Msg", "Meldung"))
    wr.add_register(U32(30211, "Operation.Evt.Prio", "Empfohlene Aktion"))
    wr.add_register(U32(30199, "Operation.RmgTms", "Wartezeit bis Einspeisung"))
    wr.add_register(U32(30201, "Operation.Health", "Zustand"))
    wr.add_register(U32(30207, "Operation.HealthStt.Alm", "Nennleistung im Zustand Fehler"))
    wr.add_register(U32(30203, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(U32(31085, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(U32(30205, "Operation.HealthStt.Wrn", "Nennleistung im Zustand Warnung"))
    wr.add_register(U32(30055, "Nameplate.Vendor", "Hersteller"))
    wr.add_register(U32(40077, "Sys.DevRstr", "Geräteneustart auslösen"))
    wr.add_register(U32(40647, "Upd.AutoUpdIsOn", "Automatische Updates eingeschaltet"))
    wr.add_register(U32(40013, "CntrySettings.Lang", "Sprache der Oberfläche"))
    wr.add_register(U32(40005, "DtTm.DlSvIsOn", "Automatische Sommer-/Winterzeitumstellung eingeschaltet"))
    wr.add_register(U32(40003, "DtTm.TmZn", "Zeitzone"))
    wr.add_register(U32(40575, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(U32(40577, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(U32(30875, "MltFncSw.Stt", "Status des Multifunktionsrelais"))
    wr.add_register(STR32(31041, "Spdwr.ActlDnsSrvIp", "-"))
    wr.add_register(STR32(31033, "Spdwr.ActlGwIp", "-"))
    wr.add_register(STR32(31017, "Spdwr.ActlIp", "-"))
    wr.add_register(STR32(31025, "Spdwr.ActlSnetMsk", "-"))
    wr.add_register(U32(30925, "Spdwr.ComSocA.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM A"))
    wr.add_register(U32(30927, "Spdwr.ComSocA.DpxMode", "Duplexmodus von SMACOM A"))
    wr.add_register(U32(30929, "Spdwr.ComSocA.Stt", "Speedwire-Verbindungsstatus von SMACOM A"))
    wr.add_register(U32(30931, "Spdwr.ComSocB.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM B"))
    wr.add_register(U32(30933, "Spdwr.ComSocB.DpxMode", "Duplexmodus von SMACOM B"))
    wr.add_register(U32(30935, "Spdwr.ComSocB.Stt", "Speedwire-Verbindungsstatus von SMACOM B"))
    wr.add_register(U32(40157, "Spdwr.AutoCfgIsOn", "Automatische Speedwire-Konfiguration eingeschaltet"))
    wr.add_register(STR32(40159, "Spdwr.Ip", "-"))
    wr.add_register(STR32(40167, "Spdwr.SnetMsk", "-"))
    wr.add_register(STR32(40513, "Spdwr.DnsSrvIp", "-"))
    wr.add_register(STR32(40175, "Spdwr.GwIp", "-"))
    wr.add_register(S32(34609, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34625, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34627, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34611, "Env.TmpValMax", "Höchste gemessene Außentemperatur"))
    wr.add_register(S32(34621, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(S32(34629, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(S32(34631, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(U32(34615, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34633, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34635, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34623, "Env.ExInsol", "Einstrahlung auf externen Sensor"))
    wr.add_register(U64(30517, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30535, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30537, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30539, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(31447, "Metering.GridMs.Hz", "Netzfrequenz"))
    wr.add_register(S32(31435, "Metering.GridMs.A.phsA", "Ausgangsstrom Netzeinspeisung Phase L1"))
    wr.add_register(S32(31437, "Metering.GridMs.A.phsB", "Ausgangsstrom Netzeinspeisung Phase L2"))
    wr.add_register(S32(31439, "Metering.GridMs.A.phsC", "Ausgangsstrom Netzeinspeisung Phase L3"))
    wr.add_register(U32(31451, "Metering.GridMs.PhV.phsA2B", "Netzspannung Phase L1 gegen L2"))
    wr.add_register(U32(31453, "Metering.GridMs.PhV.phsB2C", "Netzspannung Phase L2 gegen L3"))
    wr.add_register(U32(31449, "Metering.GridMs.PhV.phsC2A", "Netzspannung Phase L3 gegen L1"))
    wr.add_register(U32(31253, "Metering.GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(31255, "Metering.GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(31257, "Metering.GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(31259, "Metering.GridMs.W.phsA", "Leistung Netzeinspeisung L1"))
    wr.add_register(U32(31261, "Metering.GridMs.W.phsB", "Leistung Netzeinspeisung L2"))
    wr.add_register(U32(31263, "Metering.GridMs.W.phsC", "Leistung Netzeinspeisung L3"))
    wr.add_register(U32(31265, "Metering.GridMs.WIn.phsA", "Leistung Netzbezug Phase L1"))
    wr.add_register(U32(31267, "Metering.GridMs.WIn.phsB", "Leistung Netzbezug Phase L2"))
    wr.add_register(U32(31269, "Metering.GridMs.WIn.phsC", "Leistung Netzbezug Phase L3"))
    wr.add_register(S32(31271, "Metering.GridMs.VAr.phsA", "Blindleistung Netzeinspeisung Phase L1"))
    wr.add_register(S32(31273, "Metering.GridMs.VAr.phsB", "Blindleistung Netzeinspeisung Phase L2"))
    wr.add_register(S32(31275, "Metering.GridMs.VAr.phsC", "Blindleistung Netzeinspeisung Phase L3"))
    wr.add_register(S32(31277, "Metering.GridMs.TotVAr", "Blindleistung Netzeinspeisung"))
    wr.add_register(S32(31441, "Metering.GridMs.VA.phsA", "Scheinleistung L1"))
    wr.add_register(S32(31443, "Metering.GridMs.VA.phsB", "Scheinleistung L2"))
    wr.add_register(S32(31445, "Metering.GridMs.VA.phsC", "Scheinleistung L3"))
    wr.add_register(S32(31455, "Metering.GridMs.TotVA", "Scheinleistung"))
    wr.add_register(U32(31433, "Metering.GridMs.TotPF", "Verschiebungsfaktor"))
    wr.add_register(S32(31499, "Metering.GridMs.TotPFEEI", "EEI-Verschiebungsfaktor"))
    wr.add_register(S32(30867, "Metering.GridMs.TotWOut", "Leistung Einspeisung"))
    wr.add_register(U32(30583, "Metering.GridMs.TotWhOut", "Zählerstand Einspeisezähler"))
    wr.add_register(S32(30865, "Metering.GridMs.TotWIn", "Leistung Bezug"))
    wr.add_register(U32(30581, "Metering.GridMs.TotWhIn", "Zählerstand Bezugszähler"))
    wr.add_register(
        U32(41187, "Inverter.CtlComCfg.CtlMsSrc", "Quelle der Referenzmessung zur Blind-/Wirkleistungsregelung")
    )
    wr.add_register(
        S32(
            41215,
            "Inverter.WModCfg.WCtlComCfg.FlbWSpt",
            "Externe Wirkleistungsvorgabe, Rückfallwert der Wirkleistungsvorgabe",
        )
    )
    wr.add_register(U32(31061, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(U32(34669, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(
        U32(40151, "Inverter.WModCfg.WCtlComCfg.WCtlComAct", "Wirk- und Blindleistungsregelung über Kommunikation")
    )
    wr.add_register(
        U32(44427, "Inverter.WModCfg.WCtlComCfg.WCtlComAct", "Wirk- und Blindleistungsregelung über Kommunikation")
    )
    wr.add_register(S32(40149, "Inverter.WModCfg.WCtlComCfg.WSpt", "Wirkleistungsvorgabe"))
    wr.add_register(S32(44425, "Inverter.WModCfg.WCtlComCfg.WSpt", "Wirkleistungsvorgabe"))
    wr.add_register(U32(40003, "DtTm.TmZn", "Zeitzone"))
    wr.add_register(U32(41155, "DcCfg.StrTms", "Startverzögerung Eingang"))
    wr.add_register(U32(41157, "DcCfg.StrTms", "Startverzögerung Eingang"))
    wr.add_register(U32(41131, "DcCfg.StrVol", "minimale Spannung Eingang"))
    wr.add_register(U32(41133, "DcCfg.StrVol", "minimale Spannung Eingang"))
    wr.add_register(S32(30769, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(30957, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(31793, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(31795, "DcMs.Amp", "DC Strom Eingang"))
    wr.add_register(S32(30771, "DcMs.Vol", "DC Spannung Eingang"))
    wr.add_register(S32(30959, "DcMs.Vol", "DC Spannung Eingang"))
    wr.add_register(S32(30773, "DcMs.Watt", "DC Leistung Eingang"))
    wr.add_register(S32(30961, "DcMs.Watt", "DC Leistung Eingang"))
    wr.add_register(U32(30803, "GridMs.Hz", "Netzfrequenz"))
    wr.add_register(S32(30813, "GridMs.TotVA", "Scheinleistung"))
    wr.add_register(S32(31497, "GridMs.TotVAr", "Blindleistung"))
    wr.add_register(S32(30775, "GridMs.TotW", "Leistung"))
    wr.add_register(S32(30977, "GridMs.A.phsA", "Netzstrom Phase L1"))
    wr.add_register(S32(30979, "GridMs.A.phsB", "Netzstrom Phase L2"))
    wr.add_register(S32(30981, "GridMs.A.phsC", "Netzstrom Phase L3"))
    wr.add_register(U32(30783, "GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(30785, "GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(30787, "GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(30789, "GridMs.PhV.phsA2B", "Netzspannung Phase L1 gegen L2"))
    wr.add_register(U32(30791, "GridMs.PhV.phsB2C", "Netzspannung Phase L2 gegen L3"))
    wr.add_register(U32(30793, "GridMs.PhV.phsC2A", "Netzspannung Phase L3 gegen L1"))
    wr.add_register(S32(30777, "GridMs.W.phsA", "Leistung L1"))
    wr.add_register(S32(30779, "GridMs.W.phsB", "Leistung L2"))
    wr.add_register(S32(30781, "GridMs.W.phsC", "Leistung L3"))
    wr.add_register(S32(30815, "GridMs.VA.phsA", "Scheinleistung L1"))
    wr.add_register(S32(30817, "GridMs.VA.phsB", "Scheinleistung L2"))
    wr.add_register(S32(30819, "GridMs.VA.phsC", "Scheinleistung L3"))
    wr.add_register(S32(30807, "GridMs.VAr.phsA", "Blindleistung L1"))
    wr.add_register(S32(30809, "GridMs.VAr.phsB", "Blindleistung L2"))
    wr.add_register(S32(30811, "GridMs.VAr.phsC", "Blindleistung L3"))
    wr.add_register(U32(30949, "GridMs.TotPFPrc", "Verschiebungsfaktor"))
    wr.add_register(S32(31221, "GridMs.TotPFEEI", "EEI-Verschiebungsfaktor"))
    wr.add_register(U32(30823, "GridMs.TotPFExt", "Erregungsart des cos φ"))
    wr.add_register(S32(31247, "Isolation.FltA", "Fehlerstrom"))
    wr.add_register(U32(30225, "Isolation.LeakRis", "Isolationswiderstand"))
    wr.add_register(U64(30521, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U32(30541, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U32(41173, "Metering.TotOpTmhSet", "Setze Gesamte Betriebszeit am Netzanschlusspunkt"))
    wr.add_register(U64(30525, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U32(30543, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U64(30513, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30529, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30531, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30533, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(41171, "Metering.TotkWhOutSet", "Setze Gesamtertrag"))
    wr.add_register(U32(40789, "Nameplate.ComRev", "Kommunikationsversion"))
    wr.add_register(STR32(40631, "Nameplate.Location", "-"))
    wr.add_register(U32(30057, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(40067, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(30051, "Nameplate.MainModel", "Geräteklasse"))
    wr.add_register(U32(30053, "Nameplate.Model", "Gerätetyp"))
    wr.add_register(U32(40063, "Nameplate.CmpMain.SwRev", "Firmware-Version des Hauptprozessors"))
    wr.add_register(U32(30599, "Operation.GriSwCnt", "Anzahl Netzzuschaltungen"))
    wr.add_register(U32(30217, "Operation.GriSwStt", "Netzrelais/-schütz"))
    wr.add_register(U32(30235, "Operation.BckStt", "Status des Backup-Modus"))
    wr.add_register(U32(40109, "GridGuard.Cntry", "Eingestellter Länderdatensatz"))
    wr.add_register(U32(41121, "GridGuard.CntrySet", "Setze Länderdatensatz"))
    wr.add_register(S32(30975, "Inverter.DclVol", "Zwischenkreisspannung"))
    wr.add_register(U32(40183, "Inverter.OutPhs", "Phasenzuordnung"))
    wr.add_register(U32(40791, "Inverter.PlntCtl.IntvTmsMax", "Timeout für Kommunikationsfehlermeldung"))
    wr.add_register(U32(41217, "PCC.WMax", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(U32(41199, "PCC.WMaxNom", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(U32(41203, "Plnt.DcWRtg", "Anlagen-Nennleistung"))
    wr.add_register(U32(30881, "Operation.PvGriConn", "Netzanbindung der Anlage"))
    wr.add_register(S32(30953, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(S32(34113, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(U32(30795, "GridMs.TotA", "Netzstrom"))
    wr.add_register(U32(40029, "Operation.OpStt", "Allgemeiner Betriebszustand"))
    wr.add_register(U32(30251, "Operation.RstrLokStt", "Verriegelungsstatus"))
    wr.add_register(U32(33001, "Operation.StandbyStt", "Standby-Status"))
    wr.add_register(U32(33003, "Operation.RunStt", "Betriebsstatus"))
    wr.add_register(U32(40007, "Operation.CtrlType", "Art der DC-Spannungsregelung"))
    wr.add_register(U32(40018, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(U32(41253, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(U32(44021, "Operation.ValRsIstl", "Betriebsdaten zurücksetzen"))
    wr.add_register(U32(30219, "Operation.DrtStt", "Grund der Leistungsreduzierung"))
    wr.add_register(U32(30837, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(U32(40212, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(S32(41251, "Inverter.WModCfg.WCtlComCfg.WMaxIn", "Begrenzung der Leistungsaufnahme in W"))
    wr.add_register(S32(44039, "Inverter.WModCfg.WCtlComCfg.WSptMaxNom", "Maximale Wirkleistung"))
    wr.add_register(
        S16(40023, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(
        S16(41255, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(
        S16(40016, "Inverter.WModCfg.WCtlComCfg.WNom", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(S32(44041, "Inverter.WModCfg.WCtlComCfg.WSptMinNom", "Minimale Wirkleistung"))
    wr.add_register(S32(41249, "Inverter.WModCfg.WCtlComCfg.WMaxInNomPrc", "Begrenzung der Wirkleistungsaufnahme in %"))
    wr.add_register(
        U32(41193, "Inverter.CtlComCfg.WCtlCom.CtlComMssMod", "Externe Wirkleistungsvorgabe, Rückfallverhalten")
    )
    wr.add_register(
        S32(
            44035,
            "Inverter.CtlComCfg.WCtlCom.FlbWMin",
            "Externe Wirkleistungsvorgabe, Rückfallwert der minimalen Wirkleistung",
        )
    )
    wr.add_register(
        S32(
            44037,
            "Inverter.CtlComCfg.WCtlCom.FlbWMax",
            "Externe Wirkleistungsvorgabe, Rückfallwert der maximalen Wirkleistung",
        )
    )
    wr.add_register(U32(41195, "Inverter.CtlComCfg.WCtlCom.TmsOut", "Externe Wirkleistungsvorgabe, Timeout"))
    wr.add_register(U32(33047, "Inverter.WModCfg.WCtlVolCfg.Crv.NumPtMax", "P(U), maximale Anzahl von Stützpunkten"))
    wr.add_register(U32(33007, "Operation.VArCtl.VArModAct", "Aktiver Blindleistungsbereich"))
    wr.add_register(S16(40022, "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc", "Externe Blindleistungsvorgabe"))
    wr.add_register(S16(41256, "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc", "Externe Blindleistungsvorgabe"))
    wr.add_register(
        S16(40015, "Inverter.VArModCfg.VArCtlComCfg.VArNom", "Normierte Blindleistungsvorgabe durch Anlagensteuerung")
    )
    wr.add_register(S32(41223, "Inverter.CtlComCfg.VArCtlCom.FlbVArNom", "Externe Blindleistungsvorgabe, Rückfallwert"))
    wr.add_register(
        U32(41219, "Inverter.CtlComCfg.VArCtlCom.CtlComMssMod", "Externe Blindleistungsvorgabe, Rückfallverhalten")
    )
    wr.add_register(U32(41221, "Inverter.CtlComCfg.VArCtlCom.TmsOut", "Externe Blindleistungsvorgabe, Timeout"))
    wr.add_register(
        S32(30827, "Inverter.VArModCfg.VArCnstCfg.VAr", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(40202, "Inverter.VArModCfg.VArCnstCfg.VAr", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(30829, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(40204, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(30921, "Inverter.VArModCfg.VArCnstCfgDmd.VAr", "Manuelle Blindleistungsvorgabe bei Nullwirkleistung")
    )
    wr.add_register(
        S32(30923, "Inverter.VArModCfg.VArCnstCfgDmd.VArNom", "Manuelle Blindleistungsvorgabe bei Nullwirkleistung")
    )
    wr.add_register(
        U16(40024, "Inverter.VArModCfg.PFCtlComCfg.PF", "Externe cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsabgabe")
    )
    wr.add_register(
        U32(
            40025, "Inverter.VArModCfg.PFCtlComCfg.PFExt", "Externe cos φ-Vorgabe, Erregungsart bei Wirkleistungsabgabe"
        )
    )
    wr.add_register(
        U32(
            44141,
            "Inverter.VArModCfg.PFCtlComCfg.PFIn",
            "Externe cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(
        U32(
            44143,
            "Inverter.VArModCfg.PFCtlComCfg.PFExtIn",
            "Externe cos φ-Vorgabe, Erregungsart bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(U32(41227, "Inverter.CtlComCfg.PFCtlCom.TmsOut", "Externe cos φ-Vorgabe, Timeout"))
    wr.add_register(U32(44099, "Inverter.CtlComCfg.PFCtlCom.TmsOut", "Externe cos φ-Vorgabe, Timeout"))
    wr.add_register(U32(41225, "Inverter.CtlComCfg.PFCtlCom.CtlComMssMod", "Externe cos φ-Vorgabe, Rückfallverhalten"))
    wr.add_register(U32(44097, "Inverter.CtlComCfg.PFCtlCom.CtlComMssMod", "Externe cos φ-Vorgabe, Rückfallverhalten"))
    wr.add_register(
        S32(
            41229,
            "Inverter.CtlComCfg.PFCtlCom.FlbPF",
            "Externe cos φ-Vorgabe, Rückfallwert des cos φ bei Wirkleistungsabgabe",
        )
    )
    wr.add_register(
        U32(
            44115,
            "Inverter.CtlComCfg.PFCtlCom.FlbPFIn",
            "Externe cos φ-Vorgabe, Rückfallwert des cos φ bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(
        U32(
            44117,
            "Inverter.CtlComCfg.PFCtlCom.FlbPFExtIn",
            "Externe cos φ-Vorgabe, Rückfallwert der Erregungsart bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(U32(33013, "Inverter.VArModCfg.VArCtlWCfg.Crv.NumPtMax", "Q(P), maximale Anzahl von Stützpunkten"))
    wr.add_register(
        U32(33045, "Inverter.VArModCfg.VArCtlVolCfg.Crv.NumPtMax", "Q(U), maximale Anzahl von Stützpunkten")
    )
    wr.add_register(
        U32(44211, "Inverter.VArModCfg.VArCtlVolCfg.VolRef.VolRefPu", "Q(U), Externe Bezugsspannungsvorgabe")
    )
    wr.add_register(
        U32(
            44193,
            "Inverter.CtlComCfg.VArCtlVolCom.CtlComMssMod",
            "Q(U), Rückfallverhalten bei ausbleibender Bezugsspannungsvorgabe",
        )
    )
    wr.add_register(U32(44195, "Inverter.CtlComCfg.VArCtlVolCom.FlbVolRefPu", "Q(U), Rückfallbezugsspannung"))
    wr.add_register(
        U32(44197, "Inverter.CtlComCfg.VArCtlVolCom.TmsOut", "Q(U), Timeout für ausbleibende Bezugsspannungsvorgabe")
    )
    wr.add_register(
        U32(33015, "Inverter.VArModCfg.PFCtlWCfg.Crv.NumPtMax", "cos φ(P), maximale Anzahl von Stützpunkten")
    )
    wr.add_register(
        U32(33011, "Inverter.VArModCfg.PFCtlVolCfg.Crv.NumPtMax", "cos φ(U), Maximale Anzahl von Stützpunkten")
    )
    wr.add_register(U32(30231, "Inverter.WLim", "Bemessungswirkleistung WMaxOutRtg"))
    wr.add_register(S32(33019, "Inverter.WMaxInRtg", "Bemessungswirkleistung WMaxInRtg"))
    wr.add_register(U32(33025, "Inverter.VAMaxOutRtg", "Bemessungsscheinleistung VAMaxOutRtg"))
    wr.add_register(U32(33027, "Inverter.VAMaxInRtg", "Bemessungsscheinleistung VAMaxInRtg"))
    wr.add_register(S32(33029, "Inverter.VArMaxQ1Rtg", "Bemessungsblindleistung VArMaxQ1Rtg"))
    wr.add_register(S32(33031, "Inverter.VArMaxQ2Rtg", "Bemessungsblindleistung VArMaxQ2Rtg"))
    wr.add_register(S32(33033, "Inverter.VArMaxQ3Rtg", "Bemessungsblindleistung VArMaxQ3Rtg"))
    wr.add_register(S32(33035, "Inverter.VArMaxQ4Rtg", "Bemessungsblindleistung VArMaxQ4Rtg"))
    wr.add_register(U32(33037, "Inverter.PFMinQ1Rtg", "Bemessungs-cos φ PFMinQ1Rtg"))
    wr.add_register(U32(33039, "Inverter.PFMinQ2Rtg", "Bemessungs-cos φ PFMinQ2Rtg"))
    wr.add_register(U32(33041, "Inverter.PFMinQ3Rtg", "Bemessungs-cos φ PFMinQ3Rtg"))
    wr.add_register(U32(33043, "Inverter.PFMinQ4Rtg", "Bemessungs-cos φ PFMinQ4Rtg"))
    wr.add_register(U32(40480, "Nameplate.ARtg", "Nennstrom über alle Phasen"))
    wr.add_register(U32(30233, "Inverter.WMax", "Nennwirkleistung WMaxOut"))
    wr.add_register(U32(40915, "Inverter.WMax", "Nennwirkleistung WMaxOut"))
    wr.add_register(S32(44383, "Inverter.WMaxIn", "Nennwirkleistung WMaxIn"))
    wr.add_register(U32(44389, "Inverter.VAMaxOut", "Nennscheinleistung VAMaxOut"))
    wr.add_register(U32(44391, "Inverter.VAMaxIn", "Nennscheinleistung VAMaxIn"))
    wr.add_register(S32(44393, "Inverter.VArMaxQ1", "Nennblindleistung VArMaxQ1"))
    wr.add_register(S32(44395, "Inverter.VArMaxQ2", "Nennblindleistung VArMaxQ2"))
    wr.add_register(S32(44397, "Inverter.VArMaxQ3", "Nennblindleistung VArMaxQ3"))
    wr.add_register(S32(44399, "Inverter.VArMaxQ4", "Nennblindleistung VArMaxQ4"))
    wr.add_register(S32(44401, "Inverter.VArMaxZerWQ1", "Nennblindleistung VArMaxZerWQ1"))
    wr.add_register(S32(44403, "Inverter.VArMaxZerWQ2", "Nennblindleistung VArMaxZerWQ2"))
    wr.add_register(S32(44405, "Inverter.VArMaxZerWQ3", "Nennblindleistung VArMaxZerWQ3"))
    wr.add_register(S32(44407, "Inverter.VArMaxZerWQ4", "Nennblindleistung VArMaxZerWQ4"))
    wr.add_register(U32(44409, "Inverter.PFMinQ1", "Nenn-cos φ PFMinQ1"))
    wr.add_register(U32(44411, "Inverter.PFMinQ2", "Nenn-cos φ PFMinQ2"))
    wr.add_register(U32(44413, "Inverter.PFMinQ3", "Nenn-cos φ PFMinQ3"))
    wr.add_register(U32(44415, "Inverter.PFMinQ4", "Nenn-cos φ PFMinQ4"))
    wr.add_register(U32(41169, "GridGuard.Cntry.LeakRisMin", "Minimaler Isolationswiderstand"))
    wr.add_register(U32(44005, "Inverter.VArGraConn", "Sanftanlaufsrate Q"))
    wr.add_register(U32(44007, "Inverter.VArGraConnEna", "Sanftanlauf Q"))
    wr.add_register(U32(30839, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(U32(40214, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(U32(40472, "Inverter.PlntCtl.VRef", "Netznennspannung"))
    wr.add_register(U32(44001, "Inverter.WGraConn", "Sanftanlaufsrate P"))
    wr.add_register(U32(44003, "Inverter.WGraConnEna", "Sanftanlauf P"))
    wr.add_register(U32(44009, "GridGuard.Cntry.GriStrTms", "Zuschaltzeit nach Neustart"))
    wr.add_register(U32(44011, "Inverter.WGraRecon", "Sanftanlaufsrate P nach Netzfehler"))
    wr.add_register(U32(44013, "Inverter.WGraReconEna", "Sanftanlauf P nach Netzfehler"))
    wr.add_register(U32(44015, "GridGuard.Cntry.GriFltMonTms", "Zuschaltzeit nach Netzfehler"))
    wr.add_register(U32(44017, "GridGuard.Cntry.GriFltReConTms", "Schnellzuschaltzeit nach Kurzunterbrechung"))
    wr.add_register(U32(44019, "GridGuard.Cntry.GriFltTms", "Maximale Dauer einer Kurzunterbrechung"))
    wr.add_register(U32(40009, "Operation.OpMod", "Allgemeine Betriebsart"))
    wr.add_register(U32(41201, "Inverter.WGraMpp", "Anstiegsrate bei Einstrahlungsänderung"))
    wr.add_register(U32(44023, "Inverter.WGraMpp", "Anstiegsrate bei Einstrahlungsänderung"))
    wr.add_register(U32(30835, "Inverter.WModCfg.WMod", "Betriebsart Wirkleistungsvorgabe"))
    wr.add_register(U32(40210, "Inverter.WModCfg.WMod", "Betriebsart Wirkleistungsvorgabe"))
    wr.add_register(
        U32(44025, "Inverter.WModCfg.WCtlComCfg.Dyn.WTmEna", "Externe Wirkleistungsvorgabe, Sollwertfilter")
    )
    wr.add_register(
        U32(44027, "Inverter.WModCfg.WCtlComCfg.Dyn.WTms", "Externe Wirkleistungsvorgabe, Einstellzeit Sollwertfilter")
    )
    wr.add_register(
        U32(
            44029,
            "Inverter.WModCfg.WCtlComCfg.Dyn.WGraEna",
            "Externe Wirkleistungsvorgabe, Begrenzung der Änderungsrate",
        )
    )
    wr.add_register(U32(44031, "Inverter.WModCfg.WCtlComCfg.Dyn.WGraPos", "Externe Wirkleistungsvorgabe, Anstiegsrate"))
    wr.add_register(
        U32(44033, "Inverter.WModCfg.WCtlComCfg.Dyn.WGraNeg", "Externe Wirkleistungsvorgabe, Absenkungsrate")
    )
    wr.add_register(U32(44043, "Inverter.WModCfg.WCtlVolCfg.Ena", "P(U), Aktivierung"))
    wr.add_register(U32(44045, "Inverter.WModCfg.WCtlVolCfg.VRefMod", "P(U), Art der Bezugsspannung"))
    wr.add_register(U32(44047, "Inverter.WModCfg.WCtlVolCfg.WRefMod", "P(U), Art der Bezugswirkleistung"))
    wr.add_register(U32(44049, "Inverter.WModCfg.WCtlVolCfg.Crv.NumPt", "P(U), Anzahl verwendeter Punkte"))
    wr.add_register(U32(44051, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44053, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44055, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44057, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44059, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44061, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44063, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44065, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(S32(44067, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44069, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44071, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44073, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44075, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44077, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44079, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44081, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(U32(44083, "Inverter.WModCfg.WCtlVolCfg.WTmEna", "P(U), Sollwertfilter"))
    wr.add_register(U32(44085, "Inverter.WModCfg.WCtlVolCfg.WTms", "P(U), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44087, "Inverter.WModCfg.WCtlVolCfg.WGraEna", "P(U), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44089, "Inverter.WModCfg.WCtlVolCfg.WGraPos", "P(U), Anstiegsrate"))
    wr.add_register(U32(44091, "Inverter.WModCfg.WCtlVolCfg.WGraNeg", "P(U), Absenkungsrate"))
    wr.add_register(U32(44093, "Inverter.WModCfg.WCtlVolCfg.ActTms", "P(U), Auslöseverzögerung"))
    wr.add_register(
        U32(44095, "Inverter.VArModCfg.VArNomRefMod", "Blindleistungsverfahren, Bezugsgröße für Blindleistungsvorgaben")
    )
    wr.add_register(U32(41319, "Inverter.VArModCfg.VArModOut", "Blindleistungsverfahren bei Wirkleistungsabgabe"))
    wr.add_register(U32(41321, "Inverter.VArModCfg.VArModIn", "Blindleistungsverfahren bei Wirkleistungsaufnahme"))
    wr.add_register(U32(41323, "Inverter.VArModCfg.VArModZerW", "Blindleistungsverfahren bei Nullwirkleistung"))
    wr.add_register(U32(41367, "Inverter.VArModCfg.PFMinEna", "Nenn-cos φ PFMinQ1-Q4"))
    wr.add_register(S32(41369, "Inverter.VArModCfg.OutWNomLimAct", "Aktivierungsschwelle bei Wirkleistungsabgabe"))
    wr.add_register(S32(41371, "Inverter.VArModCfg.OutWNomLimDeAct", "Deaktivierungsschwelle bei Wirkleistungsabgabe"))
    wr.add_register(S32(41373, "Inverter.VArModCfg.InWNomLimAct", "Aktivierungsschwelle bei Wirkleistungsaufnahme"))
    wr.add_register(S32(41375, "Inverter.VArModCfg.InWNomLimDeAct", "Deaktivierungsschwelle bei Wirkleistungsaufnahme"))
    wr.add_register(U32(44101, "Inverter.VArModCfg.VArCfg.Dyn.VArTmEna", "Blindleistungsvorgabe, Sollwertfilter"))
    wr.add_register(
        U32(44103, "Inverter.VArModCfg.VArCfg.Dyn.VArTms", "Blindleistungsvorgabe, Einstellzeit Sollwertfilter")
    )
    wr.add_register(
        U32(44105, "Inverter.VArModCfg.VArCfg.Dyn.VArGraEna", "Blindleistungsvorgabe, Begrenzung der Änderungsrate")
    )
    wr.add_register(U32(44107, "Inverter.VArModCfg.VArCfg.Dyn.VArGraPos", "Blindleistungsvorgabe, Anstiegsrate"))
    wr.add_register(U32(44109, "Inverter.VArModCfg.VArCfg.Dyn.VArGraNeg", "Blindleistungsvorgabe, Absenkungsrate"))
    wr.add_register(
        U32(44119, "Inverter.VArModCfg.PFCnstCfg.PFIn", "Manuelle cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsbezug")
    )
    wr.add_register(
        U32(
            44121, "Inverter.VArModCfg.PFCnstCfg.PFExtIn", "Manuelle cos φ-Vorgabe, Erregungsart bei Wirkleistungsbezug"
        )
    )
    wr.add_register(
        U32(44123, "Inverter.VArModCfg.PFCfg.Dyn.WFilTmEna", "cos φ-Vorgabe, Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(
        U32(44125, "Inverter.VArModCfg.PFCfg.Dyn.WFilTms", "cos φ-Vorgabe, Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44127, "Inverter.VArModCfg.PFCfg.Dyn.VArTmEna", "cos φ-Vorgabe, Sollwertfilter"))
    wr.add_register(U32(44129, "Inverter.VArModCfg.PFCfg.Dyn.VArTms", "cos φ-Vorgabe, Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44131, "Inverter.VArModCfg.PFCfg.Dyn.VArGraEna", "cos φ-Vorgabe, Begrenzung der Änderungsrate"))
    wr.add_register(U32(44133, "Inverter.VArModCfg.PFCfg.Dyn.VArGraPos", "cos φ-Vorgabe, Anstiegsrate"))
    wr.add_register(U32(44135, "Inverter.VArModCfg.PFCfg.Dyn.VArGraNeg", "cos φ-Vorgabe, Absenkungsrate"))
    wr.add_register(U32(44145, "Inverter.VArModCfg.VArCtlWCfg.Crv.NumPt", "Q(P), Anzahl verwendeter Stützpunkte"))
    wr.add_register(S32(44147, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44149, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44151, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44153, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44155, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44157, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44159, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44161, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44163, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44165, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44167, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44169, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44171, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44173, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44175, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44177, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(U32(44179, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArTmEna", "Q(P), Sollwertfilter"))
    wr.add_register(U32(44181, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArTms", "Q(P), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44183, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraEna", "Q(P), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44185, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraPos", "Q(P), Anstiegsrate"))
    wr.add_register(U32(44187, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraNeg", "Q(P), Absenkungsrate"))
    wr.add_register(U32(44189, "Inverter.VArModCfg.VArCtlWCfg.Dyn.ActTms", "Q(P), Auslöseverzögerung"))
    wr.add_register(U32(44191, "Inverter.VArModCfg.VArCtlVolCfg.Crv.NumPt", "Q(U), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(41303, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41325, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41327, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41329, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41331, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41333, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41335, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41337, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41339, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(S32(41305, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41341, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41343, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41345, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41347, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41349, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41351, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41353, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41355, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(
        U32(
            41311,
            "Inverter.VArModCfg.VArCtlVolCfg.VolRef.AutnAdjMod",
            "Q(U), Betriebsart der Bezugsspannungsanpassung ",
        )
    )
    wr.add_register(
        U32(
            41313,
            "Inverter.VArModCfg.VArCtlVolCfg.VolRef.AutnAdjTms",
            "Q(U), Einstellzeit der automatischen Bezugsspannungsanpassung",
        )
    )
    wr.add_register(U32(44199, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArTmEna", "Q(U), Sollwertfilter"))
    wr.add_register(U32(44201, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArTms", "Q(U), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44203, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraEna", "Q(U), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44205, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraPos", "Q(U), Anstiegsrate"))
    wr.add_register(U32(44207, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraNeg", "Q(U), Absenkungsrate"))
    wr.add_register(U32(44209, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.ActTms", "Q(U), Auslöseverzögerung"))
    wr.add_register(U32(44213, "Inverter.VArModCfg.PFCtlWCfg.Crv.NumPt", "cos φ(P), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(44215, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44217, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44219, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44221, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44223, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44225, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44227, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44229, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(S32(44231, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44233, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44235, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44237, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(
        U32(44239, "Inverter.VArModCfg.PFCtlWCfg.Dyn.WFilTmEna", "cos φ(P), Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44241, "Inverter.VArModCfg.PFCtlWCfg.Dyn.WFilTms", "cos φ(P), Einstellzeit Istwertfilter"))
    wr.add_register(U32(44243, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArTmEna", "cos φ(P), Sollwertfilter"))
    wr.add_register(U32(44245, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArTms", "cos φ(P), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44247, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraEna", "cos φ(P), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44249, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraPos", "cos φ(P), Anstiegsrate"))
    wr.add_register(U32(44251, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraNeg", "cos φ(P), Absenkungsrate"))
    wr.add_register(U32(44253, "Inverter.VArModCfg.PFCtlWCfg.Dyn.ActTms", "cos φ(P), Auslöseverzögerung"))
    wr.add_register(U32(44255, "Inverter.VArModCfg.PFCtlVolCfg.Crv.NumPt", "cos φ(U), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(44257, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44259, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44261, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44263, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44265, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44267, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44269, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44271, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44273, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44275, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44277, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44279, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(
        U32(44281, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.WFilTmEna", "cos φ(U), Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44283, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.WFilTms", "cos φ(U), Einstellzeit Istwertfilter"))
    wr.add_register(U32(44285, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArTmEna", "cos φ(U), Sollwertfilter"))
    wr.add_register(U32(44287, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArTms", "cos φ(U), Einstellzeit Sollwertfilter"))
    wr.add_register(
        U32(44289, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraEna", "cos φ(U), Begrenzung der Änderungsrate")
    )
    wr.add_register(U32(44291, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraPos", "cos φ(U), Anstiegsrate"))
    wr.add_register(U32(44293, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraNeg", "cos φ(U), Absenkungsrate"))
    wr.add_register(U32(44295, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.ActTms", "cos φ(U), Auslöseverzögerung"))
    wr.add_register(U32(44297, "GridGuard.Cntry.VolCtl.MaxPu", "Spannungsüberwachung, obere Maximalschwelle"))
    wr.add_register(
        U32(44303, "GridGuard.Cntry.VolCtl.MaxPuTmms", "Spannungsüberwachung, obere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44299, "GridGuard.Cntry.VolCtl.hhLimPu", "Spannungsüberwachung, mittlere Maximalschwelle"))
    wr.add_register(
        U32(40450, "GridGuard.Cntry.VolCtl.hhLimTmms", "Spannungsüberwachung, mittlere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44301, "GridGuard.Cntry.VolCtl.hLimPu", "Spannungsüberwachung, untere Maximalschwelle"))
    wr.add_register(
        U32(40456, "GridGuard.Cntry.VolCtl.hLimTmms", "Spannungsüberwachung, untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44309, "GridGuard.Cntry.VolCtl.lLimPu", "Spannungsüberwachung, obere Minimalschwelle"))
    wr.add_register(
        U32(40462, "GridGuard.Cntry.VolCtl.lLimTmms", "Spannungsüberwachung, obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44307, "GridGuard.Cntry.VolCtl.llLimPu", "Spannungsüberwachung, mittlere Minimalschwelle"))
    wr.add_register(
        U32(40466, "GridGuard.Cntry.VolCtl.llLimTmms", "Spannungsüberwachung, mittlere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44305, "GridGuard.Cntry.VolCtl.MinPu", "Spannungsüberwachung, untere Minimalschwelle"))
    wr.add_register(
        U32(40468, "GridGuard.Cntry.VolCtl.MinTmms", "Spannungsüberwachung, untere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44311, "GridGuard.Cntry.VolCtl.ReconMaxPu", "Maximale Zuschaltspannung"))
    wr.add_register(U32(44313, "GridGuard.Cntry.VolCtl.ReconMinPu", "Minimale Zuschaltspannung"))
    wr.add_register(U32(44315, "GridGuard.Cntry.VolCtl.MaxPeakPu", "Spannungsüberwachung, Spitzenspannungsschwelle"))
    wr.add_register(
        U32(44317, "GridGuard.Cntry.VolCtl.MaxPeakTmms", "Spannungsüberwachung,  Spitzenspannungsschwelle Auslösezeit")
    )
    wr.add_register(U32(40250, "Inverter.DGSModCfg.DGSMod", "Dynamische Netzstützung, Betriebsart"))
    wr.add_register(
        U32(44319, "Inverter.DGSModCfg.ZerCurOvVolPu", "Dynamische Netzstützung, Überspannungsschwelle für Nullstrom")
    )
    wr.add_register(
        U32(44321, "Inverter.DGSModCfg.ZerCurUnVolPu", "Dynamische Netzstützung, Unterspannungsschwelle für Nullstrom")
    )
    wr.add_register(U32(44323, "Inverter.DGSModCfg.HystVolPu", "Dynamische Netzstützung, Hysteresespannung"))
    wr.add_register(U32(40103, "GridGuard.Cntry.FrqCtl.Max", "Frequenzüberwachung, obere Maximalschwelle"))
    wr.add_register(
        U32(40426, "GridGuard.Cntry.FrqCtl.MaxTmms", "Frequenzüberwachung, obere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40432, "GridGuard.Cntry.FrqCtl.hLim", "Frequenzüberwachung, untere Maximalschwelle"))
    wr.add_register(
        U32(40434, "GridGuard.Cntry.FrqCtl.hLimTmms", "Frequenzüberwachung, untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40436, "GridGuard.Cntry.FrqCtl.lLim", "Frequenzüberwachung, obere Minimalschwelle"))
    wr.add_register(
        U32(40438, "GridGuard.Cntry.FrqCtl.lLimTmms", "Frequenzüberwachung, obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(40101, "GridGuard.Cntry.FrqCtl.Min", "Frequenzüberwachung, untere Minimalschwelle"))
    wr.add_register(
        U32(40444, "GridGuard.Cntry.FrqCtl.MinTmms", "Frequenzüberwachung, untere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(41127, "GridGuard.Cntry.FrqCtl.ReconMin", "Minimale Zuschaltfrequenz"))
    wr.add_register(U32(41129, "GridGuard.Cntry.FrqCtl.ReconMax", "Maximale Zuschaltfrequenz"))
    wr.add_register(U32(44333, "Inverter.WCtlHzModCfg.Ena", "P(f)-Kennlinie"))
    wr.add_register(U32(44335, "Inverter.WCtlHzModCfg.RefModOv", "P(f), Bezugsgröße für Wirkleistung bei Überfrequenz"))
    wr.add_register(
        U32(44337, "Inverter.WCtlHzModCfg.RefModUn", "P(f), Bezugsgröße für Wirkleistung bei Unterfrequenz")
    )
    wr.add_register(U32(44339, "Inverter.WCtlHzModCfg.WTms", "P(f), Einstellzeit"))
    wr.add_register(U32(44341, "Inverter.WCtlHzModCfg.WCtlHzCfg.HystEnaOv", "P(f), Hysterese bei Überfrequenz"))
    wr.add_register(U32(44343, "Inverter.WCtlHzModCfg.WCtlHzCfg.HystEnaUn", "P(f), Hysterese bei Unterfrequenz"))
    wr.add_register(U32(44345, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(U32(44347, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(U32(44349, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(
        S32(44351, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(
        S32(44353, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(
        S32(44355, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(S32(44359, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(S32(44361, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(S32(44363, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(
        S32(44365, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(
        S32(44367, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(
        S32(44369, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(S32(44371, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnStop", "P(f), Rücksetzunterfrequenz"))
    wr.add_register(U32(44373, "Inverter.WCtlHzModCfg.WCtlHzCfg.WCtlTmms", "P(f), Auslöseverzögerung"))
    wr.add_register(U32(44375, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStopWGraTms", "P(f), Nachlaufzeit"))
    wr.add_register(
        U32(40242, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStopWGra", "P(f), Wirkleistungsänderungsrate nach Fehlerende")
    )
    wr.add_register(U32(44377, "GridGuard.Cntry.Aid.HzMon.Stt", "Inselnetzerkennung, Status der Frequenzüberwachung"))
    wr.add_register(
        U32(44379, "GridGuard.Cntry.Aid.HzMon.HzMonTmms", "Inselnetzerkennung, Auslösezeit der Frequenzüberwachung")
    )
    wr.add_register(U32(40135, "GridGuard.Cntry.HzRtg", "Nennfrequenz"))
    wr.add_register(U32(30001, "-", "Versionsnummer SMA Modbus-Profil"))
    wr.add_register(U32(30003, "Nameplate.SusyId", "SUSyID Modul"))
    wr.add_register(U32(30005, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U64(42109, "-", "Unit ID des Wechselrichters"))
    wr.add_register(U32(43090, "-", "SMA Grid Guard-Code"))
    wr.add_register(U32(30055, "Nameplate.Vendor", "Hersteller"))
    wr.add_register(U32(30193, "DtTm.Tm", "Systemzeit"))


# Modbus registers for SBS3.7-10 / SBS5.0-10 / SBS6.0-10 (V13)


def add_sbstorage_register(wr: Modbus):
    wr.add_register(STR32(40497, "Nameplate.MacId", "-"))
    wr.add_register(U32(30059, "Nameplate.PkgRev", "Softwarepaket"))
    wr.add_register(U32(30559, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U64(35377, "Operation.EvtCntUsr", "Anzahl Ereignisse für Benutzer"))
    wr.add_register(U32(30561, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U64(35381, "Operation.EvtCntIstl", "Anzahl Ereignisse für Installateur"))
    wr.add_register(U32(30563, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U64(35385, "Operation.EvtCntSvc", "Anzahl Ereignisse für Service"))
    wr.add_register(U32(30215, "Operation.Evt.Dsc", "Fehlerbehebungsmaßnahme"))
    wr.add_register(U32(30247, "Operation.Evt.EvtNo", "Aktuelle Ereignisnummer für Hersteller"))
    wr.add_register(U32(30213, "Operation.Evt.Msg", "Meldung"))
    wr.add_register(U32(30211, "Operation.Evt.Prio", "Empfohlene Aktion"))
    wr.add_register(U32(30199, "Operation.RmgTms", "Wartezeit bis Einspeisung"))
    wr.add_register(U32(30201, "Operation.Health", "Zustand"))
    wr.add_register(U32(30207, "Operation.HealthStt.Alm", "Nennleistung im Zustand Fehler"))
    wr.add_register(U32(30203, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(U32(31085, "Operation.HealthStt.Ok", "Nennleistung im Zustand Ok"))
    wr.add_register(U32(30205, "Operation.HealthStt.Wrn", "Nennleistung im Zustand Warnung"))
    wr.add_register(U32(30055, "Nameplate.Vendor", "Hersteller"))
    wr.add_register(U32(40077, "Sys.DevRstr", "Geräteneustart auslösen"))
    wr.add_register(U32(40647, "Upd.AutoUpdIsOn", "Automatische Updates eingeschaltet"))
    wr.add_register(U32(40013, "CntrySettings.Lang", "Sprache der Oberfläche"))
    wr.add_register(U32(40005, "DtTm.DlSvIsOn", "Automatische Sommer-/Winterzeitumstellung eingeschaltet"))
    wr.add_register(U32(40003, "DtTm.TmZn", "Zeitzone"))
    wr.add_register(U32(40575, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(U32(40577, "MltFncSw.OpMode", "Betriebsart des Multifunktionsrelais"))
    wr.add_register(U32(30875, "MltFncSw.Stt", "Status des Multifunktionsrelais"))
    wr.add_register(STR32(31041, "Spdwr.ActlDnsSrvIp", "-"))
    wr.add_register(STR32(31033, "Spdwr.ActlGwIp", "-"))
    wr.add_register(STR32(31017, "Spdwr.ActlIp", "-"))
    wr.add_register(STR32(31025, "Spdwr.ActlSnetMsk", "-"))
    wr.add_register(U32(30925, "Spdwr.ComSocA.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM A"))
    wr.add_register(U32(30927, "Spdwr.ComSocA.DpxMode", "Duplexmodus von SMACOM A"))
    wr.add_register(U32(30929, "Spdwr.ComSocA.Stt", "Speedwire-Verbindungsstatus von SMACOM A"))
    wr.add_register(U32(30931, "Spdwr.ComSocB.ConnSpd", "Verbindungsgeschwindigkeit von SMACOM B"))
    wr.add_register(U32(30933, "Spdwr.ComSocB.DpxMode", "Duplexmodus von SMACOM B"))
    wr.add_register(U32(30935, "Spdwr.ComSocB.Stt", "Speedwire-Verbindungsstatus von SMACOM B"))
    wr.add_register(U32(40157, "Spdwr.AutoCfgIsOn", "Automatische Speedwire-Konfiguration eingeschaltet"))
    wr.add_register(STR32(40159, "Spdwr.Ip", "-"))
    wr.add_register(STR32(40167, "Spdwr.SnetMsk", "-"))
    wr.add_register(STR32(40513, "Spdwr.DnsSrvIp", "-"))
    wr.add_register(STR32(40175, "Spdwr.GwIp", "-"))
    wr.add_register(S32(34609, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34625, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34627, "Env.TmpVal", "Außentemperatur"))
    wr.add_register(S32(34611, "Env.TmpValMax", "Höchste gemessene Außentemperatur"))
    wr.add_register(S32(34621, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(S32(34629, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(S32(34631, "Mdul.TmpVal", "Modultemperatur"))
    wr.add_register(U32(34615, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34633, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34635, "Env.HorWSpd", "Windgeschwindigkeit"))
    wr.add_register(U32(34623, "Env.ExInsol", "Einstrahlung auf externen Sensor"))
    wr.add_register(U64(30517, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30535, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30537, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(30539, "Metering.DyWhOut", "Tagesertrag"))
    wr.add_register(U32(31447, "Metering.GridMs.Hz", "Netzfrequenz"))
    wr.add_register(S32(31435, "Metering.GridMs.A.phsA", "Ausgangsstrom Netzeinspeisung Phase L1"))
    wr.add_register(S32(31437, "Metering.GridMs.A.phsB", "Ausgangsstrom Netzeinspeisung Phase L2"))
    wr.add_register(S32(31439, "Metering.GridMs.A.phsC", "Ausgangsstrom Netzeinspeisung Phase L3"))
    wr.add_register(U32(31451, "Metering.GridMs.PhV.phsA2B", "Netzspannung Phase L1 gegen L2"))
    wr.add_register(U32(31453, "Metering.GridMs.PhV.phsB2C", "Netzspannung Phase L2 gegen L3"))
    wr.add_register(U32(31449, "Metering.GridMs.PhV.phsC2A", "Netzspannung Phase L3 gegen L1"))
    wr.add_register(U32(31253, "Metering.GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(31255, "Metering.GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(31257, "Metering.GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(31259, "Metering.GridMs.W.phsA", "Leistung Netzeinspeisung L1"))
    wr.add_register(U32(31261, "Metering.GridMs.W.phsB", "Leistung Netzeinspeisung L2"))
    wr.add_register(U32(31263, "Metering.GridMs.W.phsC", "Leistung Netzeinspeisung L3"))
    wr.add_register(U32(31265, "Metering.GridMs.WIn.phsA", "Leistung Netzbezug Phase L1"))
    wr.add_register(U32(31267, "Metering.GridMs.WIn.phsB", "Leistung Netzbezug Phase L2"))
    wr.add_register(U32(31269, "Metering.GridMs.WIn.phsC", "Leistung Netzbezug Phase L3"))
    wr.add_register(S32(31271, "Metering.GridMs.VAr.phsA", "Blindleistung Netzeinspeisung Phase L1"))
    wr.add_register(S32(31273, "Metering.GridMs.VAr.phsB", "Blindleistung Netzeinspeisung Phase L2"))
    wr.add_register(S32(31275, "Metering.GridMs.VAr.phsC", "Blindleistung Netzeinspeisung Phase L3"))
    wr.add_register(S32(31277, "Metering.GridMs.TotVAr", "Blindleistung Netzeinspeisung"))
    wr.add_register(S32(31441, "Metering.GridMs.VA.phsA", "Scheinleistung L1"))
    wr.add_register(S32(31443, "Metering.GridMs.VA.phsB", "Scheinleistung L2"))
    wr.add_register(S32(31445, "Metering.GridMs.VA.phsC", "Scheinleistung L3"))
    wr.add_register(S32(31455, "Metering.GridMs.TotVA", "Scheinleistung"))
    wr.add_register(U32(31433, "Metering.GridMs.TotPF", "Verschiebungsfaktor"))
    wr.add_register(S32(31499, "Metering.GridMs.TotPFEEI", "EEI-Verschiebungsfaktor"))
    wr.add_register(S32(30867, "Metering.GridMs.TotWOut", "Leistung Einspeisung"))
    wr.add_register(U32(30583, "Metering.GridMs.TotWhOut", "Zählerstand Einspeisezähler"))
    wr.add_register(S32(30865, "Metering.GridMs.TotWIn", "Leistung Bezug"))
    wr.add_register(U32(30581, "Metering.GridMs.TotWhIn", "Zählerstand Bezugszähler"))
    wr.add_register(
        U32(41187, "Inverter.CtlComCfg.CtlMsSrc", "Quelle der Referenzmessung zur Blind-/Wirkleistungsregelung")
    )
    wr.add_register(
        S32(
            41215,
            "Inverter.WModCfg.WCtlComCfg.FlbWSpt",
            "Externe Wirkleistungsvorgabe, Rückfallwert der Wirkleistungsvorgabe",
        )
    )
    wr.add_register(U32(31061, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(U32(34669, "Bat.ChaCtlComAval", "Steuerung der Batterieladung über Kommunikation verfügbar"))
    wr.add_register(
        U32(40151, "Inverter.WModCfg.WCtlComCfg.WCtlComAct", "Wirk- und Blindleistungsregelung über Kommunikation")
    )
    wr.add_register(
        U32(44427, "Inverter.WModCfg.WCtlComCfg.WCtlComAct", "Wirk- und Blindleistungsregelung über Kommunikation")
    )
    wr.add_register(S32(40149, "Inverter.WModCfg.WCtlComCfg.WSpt", "Wirkleistungsvorgabe"))
    wr.add_register(S32(44425, "Inverter.WModCfg.WCtlComCfg.WSpt", "Wirkleistungsvorgabe"))
    wr.add_register(U32(30845, "Bat.ChaStt", "Aktueller Batterieladezustand"))
    wr.add_register(U32(34659, "Operation.CmpBMS.OpStt", "Betriebsstatus"))
    wr.add_register(U32(41363, "CmpBMS.BatChaWh", "Ladeenergie"))
    wr.add_register(U32(41365, "CmpBMS.BatDschWh", "Entladeenergie"))
    wr.add_register(U32(40003, "DtTm.TmZn", "Zeitzone"))
    wr.add_register(U32(30803, "GridMs.Hz", "Netzfrequenz"))
    wr.add_register(S32(30813, "GridMs.TotVA", "Scheinleistung"))
    wr.add_register(S32(31497, "GridMs.TotVAr", "Blindleistung"))
    wr.add_register(S32(30775, "GridMs.TotW", "Leistung"))
    wr.add_register(S32(30977, "GridMs.A.phsA", "Netzstrom Phase L1"))
    wr.add_register(S32(30979, "GridMs.A.phsB", "Netzstrom Phase L2"))
    wr.add_register(S32(30981, "GridMs.A.phsC", "Netzstrom Phase L3"))
    wr.add_register(U32(30783, "GridMs.PhV.phsA", "Netzspannung Phase L1"))
    wr.add_register(U32(30785, "GridMs.PhV.phsB", "Netzspannung Phase L2"))
    wr.add_register(U32(30787, "GridMs.PhV.phsC", "Netzspannung Phase L3"))
    wr.add_register(U32(30789, "GridMs.PhV.phsA2B", "Netzspannung Phase L1 gegen L2"))
    wr.add_register(U32(30791, "GridMs.PhV.phsB2C", "Netzspannung Phase L2 gegen L3"))
    wr.add_register(U32(30793, "GridMs.PhV.phsC2A", "Netzspannung Phase L3 gegen L1"))
    wr.add_register(S32(30777, "GridMs.W.phsA", "Leistung L1"))
    wr.add_register(S32(30779, "GridMs.W.phsB", "Leistung L2"))
    wr.add_register(S32(30781, "GridMs.W.phsC", "Leistung L3"))
    wr.add_register(S32(30815, "GridMs.VA.phsA", "Scheinleistung L1"))
    wr.add_register(S32(30817, "GridMs.VA.phsB", "Scheinleistung L2"))
    wr.add_register(S32(30819, "GridMs.VA.phsC", "Scheinleistung L3"))
    wr.add_register(S32(30807, "GridMs.VAr.phsA", "Blindleistung L1"))
    wr.add_register(S32(30809, "GridMs.VAr.phsB", "Blindleistung L2"))
    wr.add_register(S32(30811, "GridMs.VAr.phsC", "Blindleistung L3"))
    wr.add_register(U32(30949, "GridMs.TotPFPrc", "Verschiebungsfaktor"))
    wr.add_register(S32(31221, "GridMs.TotPFEEI", "EEI-Verschiebungsfaktor"))
    wr.add_register(U32(30823, "GridMs.TotPFExt", "Erregungsart des cos φ"))
    wr.add_register(S32(31247, "Isolation.FltA", "Fehlerstrom"))
    wr.add_register(U32(30225, "Isolation.LeakRis", "Isolationswiderstand"))
    wr.add_register(U64(30521, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U32(30541, "Metering.TotOpTms", "Betriebszeit"))
    wr.add_register(U32(41173, "Metering.TotOpTmhSet", "Setze Gesamte Betriebszeit am Netzanschlusspunkt"))
    wr.add_register(U64(30525, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U32(30543, "Metering.TotFeedTms", "Einspeisezeit"))
    wr.add_register(U64(30513, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30529, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30531, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(30533, "Metering.TotWhOut", "Gesamtertrag"))
    wr.add_register(U32(41171, "Metering.TotkWhOutSet", "Setze Gesamtertrag"))
    wr.add_register(U32(40789, "Nameplate.ComRev", "Kommunikationsversion"))
    wr.add_register(STR32(40631, "Nameplate.Location", "-"))
    wr.add_register(U32(30057, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(40067, "Nameplate.SerNum", "Seriennummer"))
    wr.add_register(U32(30051, "Nameplate.MainModel", "Geräteklasse"))
    wr.add_register(U32(30053, "Nameplate.Model", "Gerätetyp"))
    wr.add_register(U32(40063, "Nameplate.CmpMain.SwRev", "Firmware-Version des Hauptprozessors"))
    wr.add_register(U32(30599, "Operation.GriSwCnt", "Anzahl Netzzuschaltungen"))
    wr.add_register(U32(30217, "Operation.GriSwStt", "Netzrelais/-schütz"))
    wr.add_register(S32(30975, "Inverter.DclVol", "Zwischenkreisspannung"))
    wr.add_register(U32(40109, "GridGuard.Cntry", "Eingestellter Länderdatensatz"))
    wr.add_register(U32(41121, "GridGuard.CntrySet", "Setze Länderdatensatz"))
    wr.add_register(U32(40183, "Inverter.OutPhs", "Phasenzuordnung"))
    wr.add_register(U32(30877, "Operation.CsmpGriConnStt", "Status Stromversorgung"))
    wr.add_register(U32(30915, "Operation.CsmpGriConnStt", "Status Stromversorgung"))
    wr.add_register(U32(30795, "GridMs.TotA", "Netzstrom"))
    wr.add_register(S32(30953, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(S32(34113, "Coolsys.Cab.TmpVal", "Innentemperatur"))
    wr.add_register(U32(41203, "Plnt.DcWRtg", "Anlagen-Nennleistung"))
    wr.add_register(S32(30843, "Bat.Amp", "Batteriestrom"))
    wr.add_register(S32(31461, "Bat.Amp", "Batteriestrom"))
    wr.add_register(S32(31463, "Bat.Amp", "Batteriestrom"))
    wr.add_register(U32(30851, "Bat.Vol", "Batteriespannung"))
    wr.add_register(U32(31465, "Bat.Vol", "Batteriespannung"))
    wr.add_register(U32(31467, "Bat.Vol", "Batteriespannung"))
    wr.add_register(U32(30845, "Bat.ChaStt", "Aktueller Batterieladezustand"))
    wr.add_register(U32(30847, "Bat.Diag.ActlCapacNom", "Aktuelle Batteriekapazität"))
    wr.add_register(U32(30955, "Bat.OpStt", "Betriebsstatus der Batterie"))
    wr.add_register(U32(31391, "Operation.Bat.Health", "Batterie-Zustand"))
    wr.add_register(U32(31493, "Operation.Bat.Health", "Batterie-Zustand"))
    wr.add_register(U32(31495, "Operation.Bat.Health", "Batterie-Zustand"))
    wr.add_register(U32(34659, "Operation.CmpBMS.OpStt", "Betriebsstatus"))
    wr.add_register(U32(31469, "Operation.CmpBMS.OpStt", "Betriebsstatus"))
    wr.add_register(U32(31471, "Operation.CmpBMS.OpStt", "Betriebsstatus"))
    wr.add_register(S32(30849, "Bat.TmpVal", "Batterietemperatur"))
    wr.add_register(S32(31473, "Bat.TmpVal", "Batterietemperatur"))
    wr.add_register(S32(31475, "Bat.TmpVal", "Batterietemperatur"))
    wr.add_register(U32(31389, "Nameplate.CmpBMS.SwRev", "Firmware-Version des Batteriemanagementsystems"))
    wr.add_register(U32(31477, "Nameplate.CmpBMS.SwRev", "Firmware-Version des Batteriemanagementsystems"))
    wr.add_register(U32(31479, "Nameplate.CmpBMS.SwRev", "Firmware-Version des Batteriemanagementsystems"))
    wr.add_register(STR32(41233, "Nameplate.CmpBMS.HwRevStr", "-"))
    wr.add_register(STR32(31381, "Nameplate.CmpBMS.SerNumTxt", "-"))
    wr.add_register(STR32(31481, "Nameplate.CmpBMS.SerNumTxt", "-"))
    wr.add_register(STR32(31483, "Nameplate.CmpBMS.SerNumTxt", "-"))
    wr.add_register(U32(31377, "Nameplate.Bat.Vendor", "Batterie-Hersteller"))
    wr.add_register(U32(31485, "Nameplate.Bat.Vendor", "Batterie-Hersteller"))
    wr.add_register(U32(31487, "Nameplate.Bat.Vendor", "Batterie-Hersteller"))
    wr.add_register(U32(31379, "Nameplate.CmpBMS.Typ", "Typ des Batteriemanagementsystems"))
    wr.add_register(U32(31489, "Nameplate.CmpBMS.Typ", "Typ des Batteriemanagementsystems"))
    wr.add_register(U32(31491, "Nameplate.CmpBMS.Typ", "Typ des Batteriemanagementsystems"))
    wr.add_register(U32(40187, "Bat.CapacRtgWh", "Nennkapazität der Batterie"))
    wr.add_register(U32(40073, "SelfCsmp.BatChaSttMin", "Untere Entladegrenze bei Eigenverbrauchserhöhung"))
    wr.add_register(U32(31393, "BatChrg.CurBatCha", "Momentane Batterieladung"))
    wr.add_register(U32(31395, "BatDsch.CurBatDsch", "Momentane Batterieentladung"))
    wr.add_register(U64(31397, "BatChrg.BatChrg", "Batterieladung"))
    wr.add_register(U64(31401, "BatDsch.BatDsch", "Batterieentladung"))
    wr.add_register(U32(40035, "Bat.Typ", "Batterietyp"))
    wr.add_register(U32(31057, "BatUsDm.Stt", "Status Batterienutzungsbereich"))
    wr.add_register(U32(40236, "CmpBMS.OpMod", "Betriebsart des BMS"))
    wr.add_register(U32(41259, "CmpBMS.OpMod", "Betriebsart des BMS"))
    wr.add_register(U32(40793, "CmpBMS.BatChaMinW", "Minimale Batterieladeleistung"))
    wr.add_register(U32(44431, "CmpBMS.BatChaMinW", "Minimale Batterieladeleistung"))
    wr.add_register(U32(40795, "CmpBMS.BatChaMaxW", "Maximale Batterieladeleistung"))
    wr.add_register(U32(44433, "CmpBMS.BatChaMaxW", "Maximale Batterieladeleistung"))
    wr.add_register(U32(40797, "CmpBMS.BatDschMinW", "Minimale Batterieentladeleistung"))
    wr.add_register(U32(44435, "CmpBMS.BatDschMinW", "Minimale Batterieentladeleistung"))
    wr.add_register(U32(40799, "CmpBMS.BatDschMaxW", "Maximale Batterieentladeleistung"))
    wr.add_register(U32(44437, "CmpBMS.BatDschMaxW", "Maximale Batterieentladeleistung"))
    wr.add_register(S32(40801, "CmpBMS.GridWSpt", "Sollwert der Netzaustauschleistung"))
    wr.add_register(S32(44439, "CmpBMS.GridWSpt", "Sollwert der Netzaustauschleistung"))
    wr.add_register(U32(40189, "BatConv.WMaxCha", "Maximale Ladeleistung des Batteriestellers"))
    wr.add_register(U32(40191, "BatConv.WMaxDsch", "Maximale Entladeleistung des Batteriestellers"))
    wr.add_register(U32(40719, "BatUsDm.DschProDmLim", "Untere Grenze des Tiefentladeschutzbereichs vor Abschaltung"))
    wr.add_register(U32(40721, "BatUsDm.DschProDmMin", "Minimale Breite des Tiefentladeschutzbereichs"))
    wr.add_register(U32(40725, "BatUsDm.SelfCsmpBrd", "Breite des Bereichs zur Erhaltung des Batterieladezustands"))
    wr.add_register(U32(40723, "BatUsDm.BckDmMin", "Minimale Breite des Ersatzstrombereichs"))
    wr.add_register(U32(41217, "PCC.WMax", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(U32(41199, "PCC.WMaxNom", "Eingestellte Wirkleistungsgrenze am Netzanschlusspunkt"))
    wr.add_register(U32(40029, "Operation.OpStt", "Allgemeiner Betriebszustand"))
    wr.add_register(U32(30251, "Operation.RstrLokStt", "Verriegelungsstatus"))
    wr.add_register(U32(33001, "Operation.StandbyStt", "Standby-Status"))
    wr.add_register(U32(33003, "Operation.RunStt", "Betriebsstatus"))
    wr.add_register(U32(40018, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(U32(41253, "Inverter.FstStop", "Schnellabschaltung"))
    wr.add_register(U32(44021, "Operation.ValRsIstl", "Betriebsdaten zurücksetzen"))
    wr.add_register(U32(30219, "Operation.DrtStt", "Grund der Leistungsreduzierung"))
    wr.add_register(U32(30837, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(U32(40212, "Inverter.WModCfg.WCnstCfg.W", "Wirkleistungsbegrenzung in W"))
    wr.add_register(U32(30839, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(U32(40214, "Inverter.WModCfg.WCnstCfg.WNom", "Wirkleistungsbegrenzung in %"))
    wr.add_register(S32(41251, "Inverter.WModCfg.WCtlComCfg.WMaxIn", "Begrenzung der Leistungsaufnahme in W"))
    wr.add_register(S32(44039, "Inverter.WModCfg.WCtlComCfg.WSptMaxNom", "Maximale Wirkleistung"))
    wr.add_register(
        S16(40023, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(
        S16(41255, "Inverter.WModCfg.WCtlComCfg.WNomPrc", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(
        S16(40016, "Inverter.WModCfg.WCtlComCfg.WNom", "Normierte Wirkleistungsbegrenzung durch Anlagensteuerung")
    )
    wr.add_register(S32(44041, "Inverter.WModCfg.WCtlComCfg.WSptMinNom", "Minimale Wirkleistung"))
    wr.add_register(S32(41249, "Inverter.WModCfg.WCtlComCfg.WMaxInNomPrc", "Begrenzung der Wirkleistungsaufnahme in %"))
    wr.add_register(
        U32(41193, "Inverter.CtlComCfg.WCtlCom.CtlComMssMod", "Externe Wirkleistungsvorgabe, Rückfallverhalten")
    )
    wr.add_register(
        S32(
            44035,
            "Inverter.CtlComCfg.WCtlCom.FlbWMin",
            "Externe Wirkleistungsvorgabe, Rückfallwert der minimalen Wirkleistung",
        )
    )
    wr.add_register(
        S32(
            44037,
            "Inverter.CtlComCfg.WCtlCom.FlbWMax",
            "Externe Wirkleistungsvorgabe, Rückfallwert der maximalen Wirkleistung",
        )
    )
    wr.add_register(U32(41195, "Inverter.CtlComCfg.WCtlCom.TmsOut", "Externe Wirkleistungsvorgabe, Timeout"))
    wr.add_register(U32(33047, "Inverter.WModCfg.WCtlVolCfg.Crv.NumPtMax", "P(U), maximale Anzahl von Stützpunkten"))
    wr.add_register(U32(33007, "Operation.VArCtl.VArModAct", "Aktiver Blindleistungsbereich"))
    wr.add_register(S16(40022, "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc", "Externe Blindleistungsvorgabe"))
    wr.add_register(S16(41256, "Inverter.VArModCfg.VArCtlComCfg.VArNomPrc", "Externe Blindleistungsvorgabe"))
    wr.add_register(
        S16(40015, "Inverter.VArModCfg.VArCtlComCfg.VArNom", "Normierte Blindleistungsvorgabe durch Anlagensteuerung")
    )
    wr.add_register(S32(41223, "Inverter.CtlComCfg.VArCtlCom.FlbVArNom", "Externe Blindleistungsvorgabe, Rückfallwert"))
    wr.add_register(
        U32(41219, "Inverter.CtlComCfg.VArCtlCom.CtlComMssMod", "Externe Blindleistungsvorgabe, Rückfallverhalten")
    )
    wr.add_register(U32(41221, "Inverter.CtlComCfg.VArCtlCom.TmsOut", "Externe Blindleistungsvorgabe, Timeout"))
    wr.add_register(
        S32(30827, "Inverter.VArModCfg.VArCnstCfg.VAr", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(40202, "Inverter.VArModCfg.VArCnstCfg.VAr", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(30829, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(40204, "Inverter.VArModCfg.VArCnstCfg.VArNom", "Manuelle Blindleistungsvorgabe bei Wirkleistungsabgabe")
    )
    wr.add_register(
        S32(30921, "Inverter.VArModCfg.VArCnstCfgDmd.VAr", "Manuelle Blindleistungsvorgabe bei Nullwirkleistung")
    )
    wr.add_register(
        S32(30923, "Inverter.VArModCfg.VArCnstCfgDmd.VArNom", "Manuelle Blindleistungsvorgabe bei Nullwirkleistung")
    )
    wr.add_register(
        U16(40024, "Inverter.VArModCfg.PFCtlComCfg.PF", "Externe cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsabgabe")
    )
    wr.add_register(
        U32(
            40025, "Inverter.VArModCfg.PFCtlComCfg.PFExt", "Externe cos φ-Vorgabe, Erregungsart bei Wirkleistungsabgabe"
        )
    )
    wr.add_register(
        U32(
            44141,
            "Inverter.VArModCfg.PFCtlComCfg.PFIn",
            "Externe cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(
        U32(
            44143,
            "Inverter.VArModCfg.PFCtlComCfg.PFExtIn",
            "Externe cos φ-Vorgabe, Erregungsart bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(U32(41227, "Inverter.CtlComCfg.PFCtlCom.TmsOut", "Externe cos φ-Vorgabe, Timeout"))
    wr.add_register(U32(44099, "Inverter.CtlComCfg.PFCtlCom.TmsOut", "Externe cos φ-Vorgabe, Timeout"))
    wr.add_register(U32(41225, "Inverter.CtlComCfg.PFCtlCom.CtlComMssMod", "Externe cos φ-Vorgabe, Rückfallverhalten"))
    wr.add_register(U32(44097, "Inverter.CtlComCfg.PFCtlCom.CtlComMssMod", "Externe cos φ-Vorgabe, Rückfallverhalten"))
    wr.add_register(
        S32(
            41229,
            "Inverter.CtlComCfg.PFCtlCom.FlbPF",
            "Externe cos φ-Vorgabe, Rückfallwert des cos φ bei Wirkleistungsabgabe",
        )
    )
    wr.add_register(
        U32(
            44115,
            "Inverter.CtlComCfg.PFCtlCom.FlbPFIn",
            "Externe cos φ-Vorgabe, Rückfallwert des cos φ bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(
        U32(
            44117,
            "Inverter.CtlComCfg.PFCtlCom.FlbPFExtIn",
            "Externe cos φ-Vorgabe, Rückfallwert der Erregungsart bei Wirkleistungsaufnahme",
        )
    )
    wr.add_register(U32(33013, "Inverter.VArModCfg.VArCtlWCfg.Crv.NumPtMax", "Q(P), maximale Anzahl von Stützpunkten"))
    wr.add_register(
        U32(33045, "Inverter.VArModCfg.VArCtlVolCfg.Crv.NumPtMax", "Q(U), maximale Anzahl von Stützpunkten")
    )
    wr.add_register(
        U32(44211, "Inverter.VArModCfg.VArCtlVolCfg.VolRef.VolRefPu", "Q(U), Externe Bezugsspannungsvorgabe")
    )
    wr.add_register(
        U32(
            44193,
            "Inverter.CtlComCfg.VArCtlVolCom.CtlComMssMod",
            "Q(U), Rückfallverhalten bei ausbleibender Bezugsspannungsvorgabe",
        )
    )
    wr.add_register(U32(44195, "Inverter.CtlComCfg.VArCtlVolCom.FlbVolRefPu", "Q(U), Rückfallbezugsspannung"))
    wr.add_register(
        U32(44197, "Inverter.CtlComCfg.VArCtlVolCom.TmsOut", "Q(U), Timeout für ausbleibende Bezugsspannungsvorgabe")
    )
    wr.add_register(
        U32(33015, "Inverter.VArModCfg.PFCtlWCfg.Crv.NumPtMax", "cos φ(P), maximale Anzahl von Stützpunkten")
    )
    wr.add_register(
        U32(33011, "Inverter.VArModCfg.PFCtlVolCfg.Crv.NumPtMax", "cos φ(U), Maximale Anzahl von Stützpunkten")
    )
    wr.add_register(U32(40480, "Nameplate.ARtg", "Nennstrom über alle Phasen"))
    wr.add_register(U32(33025, "Inverter.VAMaxOutRtg", "Bemessungsscheinleistung VAMaxOutRtg"))
    wr.add_register(U32(33027, "Inverter.VAMaxInRtg", "Bemessungsscheinleistung VAMaxInRtg"))
    wr.add_register(U32(30231, "Inverter.WLim", "Maximale Wirkleistung"))
    wr.add_register(S32(33019, "Inverter.WMaxInRtg", "Bemessungswirkleistung WMaxInRtg"))
    wr.add_register(S32(33029, "Inverter.VArMaxQ1Rtg", "Bemessungsblindleistung VArMaxQ1Rtg"))
    wr.add_register(S32(33031, "Inverter.VArMaxQ2Rtg", "Bemessungsblindleistung VArMaxQ2Rtg"))
    wr.add_register(S32(33033, "Inverter.VArMaxQ3Rtg", "Bemessungsblindleistung VArMaxQ3Rtg"))
    wr.add_register(S32(33035, "Inverter.VArMaxQ4Rtg", "Bemessungsblindleistung VArMaxQ4Rtg"))
    wr.add_register(U32(33037, "Inverter.PFMinQ1Rtg", "Bemessungs-cos φ PFMinQ1Rtg"))
    wr.add_register(U32(33039, "Inverter.PFMinQ2Rtg", "Bemessungs-cos φ PFMinQ2Rtg"))
    wr.add_register(U32(33041, "Inverter.PFMinQ3Rtg", "Bemessungs-cos φ PFMinQ3Rtg"))
    wr.add_register(U32(33043, "Inverter.PFMinQ4Rtg", "Bemessungs-cos φ PFMinQ4Rtg"))
    wr.add_register(U32(30233, "Inverter.WMax", "Nennwirkleistung WMaxOut"))
    wr.add_register(U32(40915, "Inverter.WMax", "Nennwirkleistung WMaxOut"))
    wr.add_register(S32(44383, "Inverter.WMaxIn", "Nennwirkleistung WMaxIn"))
    wr.add_register(U32(44389, "Inverter.VAMaxOut", "Nennscheinleistung VAMaxOut"))
    wr.add_register(U32(44391, "Inverter.VAMaxIn", "Nennscheinleistung VAMaxIn"))
    wr.add_register(S32(44393, "Inverter.VArMaxQ1", "Nennblindleistung VArMaxQ1"))
    wr.add_register(S32(44395, "Inverter.VArMaxQ2", "Nennblindleistung VArMaxQ2"))
    wr.add_register(S32(44397, "Inverter.VArMaxQ3", "Nennblindleistung VArMaxQ3"))
    wr.add_register(S32(44399, "Inverter.VArMaxQ4", "Nennblindleistung VArMaxQ4"))
    wr.add_register(S32(44401, "Inverter.VArMaxZerWQ1", "Nennblindleistung VArMaxZerWQ1"))
    wr.add_register(S32(44403, "Inverter.VArMaxZerWQ2", "Nennblindleistung VArMaxZerWQ2"))
    wr.add_register(S32(44405, "Inverter.VArMaxZerWQ3", "Nennblindleistung VArMaxZerWQ3"))
    wr.add_register(S32(44407, "Inverter.VArMaxZerWQ4", "Nennblindleistung VArMaxZerWQ4"))
    wr.add_register(U32(44409, "Inverter.PFMinQ1", "Nenn-cos φ PFMinQ1"))
    wr.add_register(U32(44411, "Inverter.PFMinQ2", "Nenn-cos φ PFMinQ2"))
    wr.add_register(U32(44413, "Inverter.PFMinQ3", "Nenn-cos φ PFMinQ3"))
    wr.add_register(U32(44415, "Inverter.PFMinQ4", "Nenn-cos φ PFMinQ4"))
    wr.add_register(U32(41169, "GridGuard.Cntry.LeakRisMin", "Minimaler Isolationswiderstand"))
    wr.add_register(U32(44005, "Inverter.VArGraConn", "Sanftanlaufsrate Q"))
    wr.add_register(U32(44007, "Inverter.VArGraConnEna", "Sanftanlauf Q"))
    wr.add_register(U32(40472, "Inverter.PlntCtl.VRef", "Netznennspannung"))
    wr.add_register(U32(44001, "Inverter.WGraConn", "Sanftanlaufsrate P"))
    wr.add_register(U32(44003, "Inverter.WGraConnEna", "Sanftanlauf P"))
    wr.add_register(U32(44009, "GridGuard.Cntry.GriStrTms", "Zuschaltzeit nach Neustart"))
    wr.add_register(U32(44011, "Inverter.WGraRecon", "Sanftanlaufsrate P nach Netzfehler"))
    wr.add_register(U32(44013, "Inverter.WGraReconEna", "Sanftanlauf P nach Netzfehler"))
    wr.add_register(U32(44015, "GridGuard.Cntry.GriFltMonTms", "Zuschaltzeit nach Netzfehler"))
    wr.add_register(U32(44017, "GridGuard.Cntry.GriFltReConTms", "Schnellzuschaltzeit nach Kurzunterbrechung"))
    wr.add_register(U32(44019, "GridGuard.Cntry.GriFltTms", "Maximale Dauer einer Kurzunterbrechung"))
    wr.add_register(U32(40009, "Operation.OpMod", "Allgemeine Betriebsart"))
    wr.add_register(U32(41201, "Inverter.WGraMpp", "Anstiegsrate bei Einstrahlungsänderung"))
    wr.add_register(U32(44023, "Inverter.WGraMpp", "Anstiegsrate bei Einstrahlungsänderung"))
    wr.add_register(U32(30835, "Inverter.WModCfg.WMod", "Betriebsart Wirkleistungsvorgabe"))
    wr.add_register(U32(40210, "Inverter.WModCfg.WMod", "Betriebsart Wirkleistungsvorgabe"))
    wr.add_register(
        U32(44025, "Inverter.WModCfg.WCtlComCfg.Dyn.WTmEna", "Externe Wirkleistungsvorgabe, Sollwertfilter")
    )
    wr.add_register(
        U32(44027, "Inverter.WModCfg.WCtlComCfg.Dyn.WTms", "Externe Wirkleistungsvorgabe, Einstellzeit Sollwertfilter")
    )
    wr.add_register(
        U32(
            44029,
            "Inverter.WModCfg.WCtlComCfg.Dyn.WGraEna",
            "Externe Wirkleistungsvorgabe, Begrenzung der Änderungsrate",
        )
    )
    wr.add_register(U32(44031, "Inverter.WModCfg.WCtlComCfg.Dyn.WGraPos", "Externe Wirkleistungsvorgabe, Anstiegsrate"))
    wr.add_register(
        U32(44033, "Inverter.WModCfg.WCtlComCfg.Dyn.WGraNeg", "Externe Wirkleistungsvorgabe, Absenkungsrate")
    )
    wr.add_register(U32(44043, "Inverter.WModCfg.WCtlVolCfg.Ena", "P(U), Aktivierung"))
    wr.add_register(U32(44045, "Inverter.WModCfg.WCtlVolCfg.VRefMod", "P(U), Art der Bezugsspannung"))
    wr.add_register(U32(44047, "Inverter.WModCfg.WCtlVolCfg.WRefMod", "P(U), Art der Bezugswirkleistung"))
    wr.add_register(U32(44049, "Inverter.WModCfg.WCtlVolCfg.Crv.NumPt", "P(U), Anzahl verwendeter Punkte"))
    wr.add_register(U32(44051, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44053, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44055, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44057, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44059, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44061, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44063, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(U32(44065, "Inverter.WModCfg.WCtlVolCfg.Crv.XVal", "P(U), Spannungswert"))
    wr.add_register(S32(44067, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44069, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44071, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44073, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44075, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44077, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44079, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(S32(44081, "Inverter.WModCfg.WCtlVolCfg.Crv.YVal", "P(U), Wirkleistungswert"))
    wr.add_register(U32(44083, "Inverter.WModCfg.WCtlVolCfg.WTmEna", "P(U), Sollwertfilter"))
    wr.add_register(U32(44085, "Inverter.WModCfg.WCtlVolCfg.WTms", "P(U), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44087, "Inverter.WModCfg.WCtlVolCfg.WGraEna", "P(U), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44089, "Inverter.WModCfg.WCtlVolCfg.WGraPos", "P(U), Anstiegsrate"))
    wr.add_register(U32(44091, "Inverter.WModCfg.WCtlVolCfg.WGraNeg", "P(U), Absenkungsrate"))
    wr.add_register(U32(44093, "Inverter.WModCfg.WCtlVolCfg.ActTms", "P(U), Auslöseverzögerung"))
    wr.add_register(
        U32(44095, "Inverter.VArModCfg.VArNomRefMod", "Blindleistungsverfahren, Bezugsgröße für Blindleistungsvorgaben")
    )
    wr.add_register(U32(41319, "Inverter.VArModCfg.VArModOut", "Blindleistungsverfahren bei Wirkleistungsabgabe"))
    wr.add_register(U32(41321, "Inverter.VArModCfg.VArModIn", "Blindleistungsverfahren bei Wirkleistungsaufnahme"))
    wr.add_register(U32(41323, "Inverter.VArModCfg.VArModZerW", "Blindleistungsverfahren bei Nullwirkleistung"))
    wr.add_register(U32(41367, "Inverter.VArModCfg.PFMinEna", "Nenn-cos φ PFMinQ1-Q4"))
    wr.add_register(S32(41369, "Inverter.VArModCfg.OutWNomLimAct", "Aktivierungsschwelle bei Wirkleistungsabgabe"))
    wr.add_register(S32(41371, "Inverter.VArModCfg.OutWNomLimDeAct", "Deaktivierungsschwelle bei Wirkleistungsabgabe"))
    wr.add_register(S32(41373, "Inverter.VArModCfg.InWNomLimAct", "Aktivierungsschwelle bei Wirkleistungsaufnahme"))
    wr.add_register(S32(41375, "Inverter.VArModCfg.InWNomLimDeAct", "Deaktivierungsschwelle bei Wirkleistungsaufnahme"))
    wr.add_register(U32(44101, "Inverter.VArModCfg.VArCfg.Dyn.VArTmEna", "Blindleistungsvorgabe, Sollwertfilter"))
    wr.add_register(
        U32(44103, "Inverter.VArModCfg.VArCfg.Dyn.VArTms", "Blindleistungsvorgabe, Einstellzeit Sollwertfilter")
    )
    wr.add_register(
        U32(44105, "Inverter.VArModCfg.VArCfg.Dyn.VArGraEna", "Blindleistungsvorgabe, Begrenzung der Änderungsrate")
    )
    wr.add_register(U32(44107, "Inverter.VArModCfg.VArCfg.Dyn.VArGraPos", "Blindleistungsvorgabe, Anstiegsrate"))
    wr.add_register(U32(44109, "Inverter.VArModCfg.VArCfg.Dyn.VArGraNeg", "Blindleistungsvorgabe, Absenkungsrate"))
    wr.add_register(
        U32(44119, "Inverter.VArModCfg.PFCnstCfg.PFIn", "Manuelle cos φ-Vorgabe, cos φ-Sollwert bei Wirkleistungsbezug")
    )
    wr.add_register(
        U32(
            44121, "Inverter.VArModCfg.PFCnstCfg.PFExtIn", "Manuelle cos φ-Vorgabe, Erregungsart bei Wirkleistungsbezug"
        )
    )
    wr.add_register(
        U32(44123, "Inverter.VArModCfg.PFCfg.Dyn.WFilTmEna", "cos φ-Vorgabe, Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(
        U32(44125, "Inverter.VArModCfg.PFCfg.Dyn.WFilTms", "cos φ-Vorgabe, Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44127, "Inverter.VArModCfg.PFCfg.Dyn.VArTmEna", "cos φ-Vorgabe, Sollwertfilter"))
    wr.add_register(U32(44129, "Inverter.VArModCfg.PFCfg.Dyn.VArTms", "cos φ-Vorgabe, Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44131, "Inverter.VArModCfg.PFCfg.Dyn.VArGraEna", "cos φ-Vorgabe, Begrenzung der Änderungsrate"))
    wr.add_register(U32(44133, "Inverter.VArModCfg.PFCfg.Dyn.VArGraPos", "cos φ-Vorgabe, Anstiegsrate"))
    wr.add_register(U32(44135, "Inverter.VArModCfg.PFCfg.Dyn.VArGraNeg", "cos φ-Vorgabe, Absenkungsrate"))
    wr.add_register(U32(44145, "Inverter.VArModCfg.VArCtlWCfg.Crv.NumPt", "Q(P), Anzahl verwendeter Stützpunkte"))
    wr.add_register(S32(44147, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44149, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44151, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44153, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44155, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44157, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44159, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44161, "Inverter.VArModCfg.VArCtlWCfg.Crv.XVal", "Q(P), Wirkleistungswert"))
    wr.add_register(S32(44163, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44165, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44167, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44169, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44171, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44173, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44175, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(S32(44177, "Inverter.VArModCfg.VArCtlWCfg.Crv.YVal", "Q(P), Blindleistungswert"))
    wr.add_register(U32(44179, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArTmEna", "Q(P), Sollwertfilter"))
    wr.add_register(U32(44181, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArTms", "Q(P), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44183, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraEna", "Q(P), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44185, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraPos", "Q(P), Anstiegsrate"))
    wr.add_register(U32(44187, "Inverter.VArModCfg.VArCtlWCfg.Dyn.VArGraNeg", "Q(P), Absenkungsrate"))
    wr.add_register(U32(44189, "Inverter.VArModCfg.VArCtlWCfg.Dyn.ActTms", "Q(P), Auslöseverzögerung"))
    wr.add_register(U32(44191, "Inverter.VArModCfg.VArCtlVolCfg.Crv.NumPt", "Q(U), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(41303, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41325, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41327, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41329, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41331, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41333, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41335, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41337, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(U32(41339, "Inverter.VArModCfg.VArCtlVolCfg.Crv.XVal", "Q(U), Spannungswert"))
    wr.add_register(S32(41305, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41341, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41343, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41345, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41347, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41349, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41351, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41353, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(S32(41355, "Inverter.VArModCfg.VArCtlVolCfg.Crv.YVal", "Q(U), Blindleistungswert"))
    wr.add_register(
        U32(
            41311,
            "Inverter.VArModCfg.VArCtlVolCfg.VolRef.AutnAdjMod",
            "Q(U), Betriebsart der Bezugsspannungsanpassung ",
        )
    )
    wr.add_register(
        U32(
            41313,
            "Inverter.VArModCfg.VArCtlVolCfg.VolRef.AutnAdjTms",
            "Q(U), Einstellzeit der automatischen Bezugsspannungsanpassung",
        )
    )
    wr.add_register(U32(44199, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArTmEna", "Q(U), Sollwertfilter"))
    wr.add_register(U32(44201, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArTms", "Q(U), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44203, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraEna", "Q(U), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44205, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraPos", "Q(U), Anstiegsrate"))
    wr.add_register(U32(44207, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.VArGraNeg", "Q(U), Absenkungsrate"))
    wr.add_register(U32(44209, "Inverter.VArModCfg.VArCtlVolCfg.Dyn.ActTms", "Q(U), Auslöseverzögerung"))
    wr.add_register(U32(44213, "Inverter.VArModCfg.PFCtlWCfg.Crv.NumPt", "cos φ(P), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(44215, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44217, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44219, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44221, "Inverter.VArModCfg.PFCtlWCfg.Crv.PFExt", "cos φ(P), Erregungsart"))
    wr.add_register(U32(44223, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44225, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44227, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(U32(44229, "Inverter.VArModCfg.PFCtlWCfg.Crv.PF", "cos φ(P), cos φ-Sollwert"))
    wr.add_register(S32(44231, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44233, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44235, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(S32(44237, "Inverter.VArModCfg.PFCtlWCfg.Crv.WNom", "cos φ(P), Wirkleistung"))
    wr.add_register(
        U32(44239, "Inverter.VArModCfg.PFCtlWCfg.Dyn.WFilTmEna", "cos φ(P), Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44241, "Inverter.VArModCfg.PFCtlWCfg.Dyn.WFilTms", "cos φ(P), Einstellzeit Istwertfilter"))
    wr.add_register(U32(44243, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArTmEna", "cos φ(P), Sollwertfilter"))
    wr.add_register(U32(44245, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArTms", "cos φ(P), Einstellzeit Sollwertfilter"))
    wr.add_register(U32(44247, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraEna", "cos φ(P), Begrenzung der Änderungsrate"))
    wr.add_register(U32(44249, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraPos", "cos φ(P), Anstiegsrate"))
    wr.add_register(U32(44251, "Inverter.VArModCfg.PFCtlWCfg.Dyn.VArGraNeg", "cos φ(P), Absenkungsrate"))
    wr.add_register(U32(44253, "Inverter.VArModCfg.PFCtlWCfg.Dyn.ActTms", "cos φ(P), Auslöseverzögerung"))
    wr.add_register(U32(44255, "Inverter.VArModCfg.PFCtlVolCfg.Crv.NumPt", "cos φ(U), Anzahl verwendeter Stützpunkte"))
    wr.add_register(U32(44257, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44259, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44261, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44263, "Inverter.VArModCfg.PFCtlVolCfg.Crv.VolPu", "cos φ(U), Spannungswert"))
    wr.add_register(U32(44265, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44267, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44269, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44271, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PFExt", "cos φ(U), Erregungsart"))
    wr.add_register(U32(44273, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44275, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44277, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(U32(44279, "Inverter.VArModCfg.PFCtlVolCfg.Crv.PF", "cos φ(U), cos φ-Sollwert"))
    wr.add_register(
        U32(44281, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.WFilTmEna", "cos φ(U), Istwertfilter für Wirkleistungsmesswert")
    )
    wr.add_register(U32(44283, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.WFilTms", "cos φ(U), Einstellzeit Istwertfilter"))
    wr.add_register(U32(44285, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArTmEna", "cos φ(U), Sollwertfilter"))
    wr.add_register(U32(44287, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArTms", "cos φ(U), Einstellzeit Sollwertfilter"))
    wr.add_register(
        U32(44289, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraEna", "cos φ(U), Begrenzung der Änderungsrate")
    )
    wr.add_register(U32(44291, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraPos", "cos φ(U), Anstiegsrate"))
    wr.add_register(U32(44293, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.VArGraNeg", "cos φ(U), Absenkungsrate"))
    wr.add_register(U32(44295, "Inverter.VArModCfg.PFCtlVolCfg.Dyn.ActTms", "cos φ(U), Auslöseverzögerung"))
    wr.add_register(U32(44297, "GridGuard.Cntry.VolCtl.MaxPu", "Spannungsüberwachung, obere Maximalschwelle"))
    wr.add_register(
        U32(44303, "GridGuard.Cntry.VolCtl.MaxPuTmms", "Spannungsüberwachung, obere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44299, "GridGuard.Cntry.VolCtl.hhLimPu", "Spannungsüberwachung, mittlere Maximalschwelle"))
    wr.add_register(
        U32(40450, "GridGuard.Cntry.VolCtl.hhLimTmms", "Spannungsüberwachung, mittlere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44301, "GridGuard.Cntry.VolCtl.hLimPu", "Spannungsüberwachung, untere Maximalschwelle"))
    wr.add_register(
        U32(40456, "GridGuard.Cntry.VolCtl.hLimTmms", "Spannungsüberwachung, untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(44309, "GridGuard.Cntry.VolCtl.lLimPu", "Spannungsüberwachung, obere Minimalschwelle"))
    wr.add_register(
        U32(40462, "GridGuard.Cntry.VolCtl.lLimTmms", "Spannungsüberwachung, obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44307, "GridGuard.Cntry.VolCtl.llLimPu", "Spannungsüberwachung, mittlere Minimalschwelle"))
    wr.add_register(
        U32(40466, "GridGuard.Cntry.VolCtl.llLimTmms", "Spannungsüberwachung, mittlere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44305, "GridGuard.Cntry.VolCtl.MinPu", "Spannungsüberwachung, untere Minimalschwelle"))
    wr.add_register(
        U32(40468, "GridGuard.Cntry.VolCtl.MinTmms", "Spannungsüberwachung, untere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(44311, "GridGuard.Cntry.VolCtl.ReconMaxPu", "Maximale Zuschaltspannung"))
    wr.add_register(U32(44313, "GridGuard.Cntry.VolCtl.ReconMinPu", "Minimale Zuschaltspannung"))
    wr.add_register(U32(44315, "GridGuard.Cntry.VolCtl.MaxPeakPu", "Spannungsüberwachung, Spitzenspannungsschwelle"))
    wr.add_register(
        U32(44317, "GridGuard.Cntry.VolCtl.MaxPeakTmms", "Spannungsüberwachung,  Spitzenspannungsschwelle Auslösezeit")
    )
    wr.add_register(U32(40250, "Inverter.DGSModCfg.DGSMod", "Dynamische Netzstützung, Betriebsart"))
    wr.add_register(
        U32(44319, "Inverter.DGSModCfg.ZerCurOvVolPu", "Dynamische Netzstützung, Überspannungsschwelle für Nullstrom")
    )
    wr.add_register(
        U32(44321, "Inverter.DGSModCfg.ZerCurUnVolPu", "Dynamische Netzstützung, Unterspannungsschwelle für Nullstrom")
    )
    wr.add_register(U32(44323, "Inverter.DGSModCfg.HystVolPu", "Dynamische Netzstützung, Hysteresespannung"))
    wr.add_register(U32(40103, "GridGuard.Cntry.FrqCtl.Max", "Frequenzüberwachung, obere Maximalschwelle"))
    wr.add_register(
        U32(40426, "GridGuard.Cntry.FrqCtl.MaxTmms", "Frequenzüberwachung, obere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40432, "GridGuard.Cntry.FrqCtl.hLim", "Frequenzüberwachung, untere Maximalschwelle"))
    wr.add_register(
        U32(40434, "GridGuard.Cntry.FrqCtl.hLimTmms", "Frequenzüberwachung, untere Maximalschwelle Auslösezeit")
    )
    wr.add_register(U32(40436, "GridGuard.Cntry.FrqCtl.lLim", "Frequenzüberwachung, obere Minimalschwelle"))
    wr.add_register(
        U32(40438, "GridGuard.Cntry.FrqCtl.lLimTmms", "Frequenzüberwachung, obere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(40101, "GridGuard.Cntry.FrqCtl.Min", "Frequenzüberwachung, untere Minimalschwelle"))
    wr.add_register(
        U32(40444, "GridGuard.Cntry.FrqCtl.MinTmms", "Frequenzüberwachung, untere Minimalschwelle Auslösezeit")
    )
    wr.add_register(U32(41127, "GridGuard.Cntry.FrqCtl.ReconMin", "Minimale Zuschaltfrequenz"))
    wr.add_register(U32(41129, "GridGuard.Cntry.FrqCtl.ReconMax", "Maximale Zuschaltfrequenz"))
    wr.add_register(U32(44333, "Inverter.WCtlHzModCfg.Ena", "P(f)-Kennlinie"))
    wr.add_register(U32(44335, "Inverter.WCtlHzModCfg.RefModOv", "P(f), Bezugsgröße für Wirkleistung bei Überfrequenz"))
    wr.add_register(
        U32(44337, "Inverter.WCtlHzModCfg.RefModUn", "P(f), Bezugsgröße für Wirkleistung bei Unterfrequenz")
    )
    wr.add_register(U32(44339, "Inverter.WCtlHzModCfg.WTms", "P(f), Einstellzeit"))
    wr.add_register(U32(44341, "Inverter.WCtlHzModCfg.WCtlHzCfg.HystEnaOv", "P(f), Hysterese bei Überfrequenz"))
    wr.add_register(U32(44343, "Inverter.WCtlHzModCfg.WCtlHzCfg.HystEnaUn", "P(f), Hysterese bei Unterfrequenz"))
    wr.add_register(S32(44371, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnStop", "P(f), Rücksetzunterfrequenz"))
    wr.add_register(S32(44359, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(S32(44361, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(S32(44363, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUn", "P(f), Knickunterfrequenz"))
    wr.add_register(
        S32(44365, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(
        S32(44367, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(
        S32(44369, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzUnGra", "P(f), Wirkleistungsänderung pro Hz bei Unterfrequenz")
    )
    wr.add_register(U32(44345, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(U32(44347, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(U32(44349, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOv", "P(f), Knicküberfrequenz"))
    wr.add_register(
        S32(44351, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(
        S32(44353, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(
        S32(44355, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzOvGra", "P(f), Wirkleistungsänderung pro Hz bei Überfrequenz")
    )
    wr.add_register(U32(44373, "Inverter.WCtlHzModCfg.WCtlHzCfg.WCtlTmms", "P(f), Auslöseverzögerung"))
    wr.add_register(U32(44375, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStopWGraTms", "P(f), Nachlaufzeit"))
    wr.add_register(
        U32(40242, "Inverter.WCtlHzModCfg.WCtlHzCfg.HzStopWGra", "P(f), Wirkleistungsänderungsrate nach Fehlerende")
    )
    wr.add_register(U32(44377, "GridGuard.Cntry.Aid.HzMon.Stt", "Inselnetzerkennung, Status der Frequenzüberwachung"))
    wr.add_register(
        U32(44379, "GridGuard.Cntry.Aid.HzMon.HzMonTmms", "Inselnetzerkennung, Auslösezeit der Frequenzüberwachung")
    )
    wr.add_register(U32(40135, "GridGuard.Cntry.HzRtg", "Nennfrequenz"))
