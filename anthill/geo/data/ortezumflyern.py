#!/usr/bin/python
# -*- coding: utf-8 -*-

orte = [
    {'ort': 'Villach', 'plz': '9500', 'treffpunkt': 'Hauptplatz', 'lat': 46.614722, 'lon': 13.846111},
    {'ort': 'Wels', 'plz': '4600', 'treffpunkt': 'Stadtplatz', 'lat': 48.1575, 'lon': 14.026667},
    {'ort': 'St. Pölten', 'plz': '3100', 'treffpunkt': 'Rathausplatz', 'lat': 48.204722, 'lon': 15.626667},
    {'ort': 'Dornbirn', 'plz': '6850', 'treffpunkt': 'Marktplatz', 'lat': 47.413417, 'lon': 9.744417},
    {'ort': 'Wiener Neustadt', 'plz': '2700', 'treffpunkt': 'Hauptplatz', 'lat': 47.816667, 'lon': 16.25},
    {'ort': 'Steyr', 'plz': '4400', 'treffpunkt': 'Stadtplatz', 'lat': 48.037222, 'lon': 14.416944},
    {'ort': 'Feldkirch', 'plz': '6800', 'treffpunkt': 'Marktgasse', 'lat': 47.238056, 'lon': 9.598333},
    {'ort': 'Bregenz', 'plz': '6900', 'treffpunkt': 'Kaiserstraße', 'lat': 47.505, 'lon': 9.749167},
    {'ort': 'Leonding', 'plz': '4060', 'treffpunkt': 'Stadtplatz', 'lat': 48.266667, 'lon': 14.25},
    {'ort': 'Klosterneuburg', 'plz': '3400', 'treffpunkt': 'Rathausplatz', 'lat': 48.305, 'lon': 16.325},
    {'ort': 'Baden', 'plz': '2500', 'treffpunkt': 'Hauptplatz', 'lat': 48.007528, 'lon': 16.234444},
    {'ort': 'Leoben', 'plz': '8700', 'treffpunkt': 'Hauptplatz', 'lat': 47.381667, 'lon': 15.097222},
    {'ort': 'Wolfsberg', 'plz': '9400', 'treffpunkt': 'Bezirkshauptmanschaft', 'lat': 46.841878, 'lon': 14.840786},
    {'ort': 'Krems', 'plz': '3500', 'treffpunkt': 'Steiner Tor', 'lat': 48.410833, 'lon': 15.610278},
    {'ort': 'Traun', 'plz': '4050', 'treffpunkt': 'Hauptplatz', 'lat': 48.221667, 'lon': 14.239722},
    {'ort': 'Amstetten', 'plz': '3300', 'treffpunkt': 'Hauptplatz', 'lat': 48.123, 'lon': 14.87213},
    {'ort': 'Kapfenberg', 'plz': '8600', 'treffpunkt': 'Hauptplatz', 'lat': 47.439444, 'lon': 15.289444},
    {'ort': 'Lustenau', 'plz': '6890', 'treffpunkt': 'Kirchplatz', 'lat': 47.4271, 'lon': 9.671139},
    {'ort': 'Hallein', 'plz': '5400', 'treffpunkt': 'Unterer Markt', 'lat': 47.683056, 'lon': 13.096944},
    {'ort': 'Mödling', 'plz': '2340', 'treffpunkt': 'Kaiserin Elisabeth Straße/Stadtgalerie', 'lat': 48.085556, 'lon': 16.283056},
    {'ort': 'Kufstein', 'plz': '6330', 'treffpunkt': 'Unterer Stadtplatz', 'lat': 47.583333, 'lon': 12.166667},
    {'ort': 'Traiskirchen', 'plz': '2512', 'treffpunkt': 'Hauptplatz', 'lat': 48.013611, 'lon': 16.295278},
    {'ort': 'Schwechat', 'plz': '2320', 'treffpunkt': 'Rathausplatz', 'lat': 48.141111, 'lon': 16.478611},
    {'ort': 'Braunau', 'plz': '5280', 'treffpunkt': 'Stadtplatz', 'lat': 48.2575, 'lon': 13.033889},
    {'ort': 'Stockerau', 'plz': '2000', 'treffpunkt': 'Rathausplatz', 'lat': 48.385833, 'lon': 16.210833},
    {'ort': 'Saalfelden', 'plz': '5760', 'treffpunkt': 'Rathausplatz', 'lat': 47.426944, 'lon': 12.848333},
    {'ort': 'Tulln', 'plz': '3430', 'treffpunkt': 'Hauptplatz', 'lat': 48.333333, 'lon': 16.05},
    {'ort': 'Ansfelden', 'plz': '4052', 'treffpunkt': 'Hauptplatz', 'lat': 48.208333, 'lon': 14.288889},
    {'ort': 'Hohenems', 'plz': '6845', 'treffpunkt': 'Jüdisches Museum', 'lat': 47.366667, 'lon': 9.666667},
    {'ort': 'Bruck an der Mur', 'plz': '8600', 'treffpunkt': 'Mittergasse/Koloman-Wallisch-Platz', 'lat': 47.410556, 'lon': 15.268889},
    {'ort': 'Spittal an der Drau', 'plz': '9800', 'treffpunkt': 'Burgplatz', 'lat': 46.797778, 'lon': 13.495556},
    {'ort': 'Telfs', 'plz': '6410', 'treffpunkt': 'Untermarktstraße/Rathaus', 'lat': 47.306944, 'lon': 11.072222},
    {'ort': 'Perchtoldsdorf', 'plz': '2380', 'treffpunkt': 'Marktplatz', 'lat': 48.119444, 'lon': 16.265},
    {'ort': 'Ternitz', 'plz': '2620', 'treffpunkt': 'Theodor-Körner-Platz/Stadthalle', 'lat': 47.716667, 'lon': 16.033333},
    {'ort': 'Eisenstadt', 'plz': '7000', 'treffpunkt': 'Hauptstraße/Cafe Central', 'lat': 47.845556, 'lon': 16.518889},
    {'ort': 'Feldkirchen', 'plz': '9560', 'treffpunkt': 'Hauptplatz', 'lat': 46.723611, 'lon': 14.091944},
    {'ort': 'Bludenz', 'plz': '6700', 'treffpunkt': 'Josef-Wolf-Platz', 'lat': 47.153333, 'lon': 9.821944},
    {'ort': 'Bad Ischl', 'plz': '4820', 'treffpunkt': 'Kaiser-Franz-Josef-Straße', 'lat': 47.711703, 'lon': 13.623015},
    {'ort': 'Hall in Tirol', 'plz': '6060', 'treffpunkt': 'Oberer Stadtplatz/Rathaus', 'lat': 47.283333, 'lon': 11.5},
    {'ort': 'Schwaz', 'plz': '6130', 'treffpunkt': 'Franz-Josef-Straße/Rathaus', 'lat': 47.344974, 'lon': 11.70822},
    {'ort': 'Feldbach', 'plz': '8330', 'treffpunkt': 'Hauptplatz', 'lat': 46.955, 'lon': 15.888333},
    {'ort': 'Wörgl', 'plz': '6300', 'treffpunkt': 'Hauptbahnhof', 'lat': 47.49085, 'lon': 12.061382},
    {'ort': 'Wals/Siezenheim', 'plz': '5071', 'treffpunkt': 'Hauptstraße/Gemeindeamt', 'lat': 47.766667, 'lon': 12.966667},
    {'ort': 'Hard', 'plz': '6971', 'treffpunkt': 'Marktstraße/Gemeindeamt', 'lat': 47.489167, 'lon': 9.69},
    {'ort': 'Gmunden', 'plz': '4810', 'treffpunkt': 'Rathausplatz', 'lat': 47.918056, 'lon': 13.799444},
    {'ort': 'Marchtrenk', 'plz': '4614', 'treffpunkt': 'Linzer Straße/Fuzo', 'lat': 48.191667, 'lon': 14.110556},
    {'ort': 'Korneuburg', 'plz': '2100', 'treffpunkt': 'Hauptplatz', 'lat': 48.345278, 'lon': 16.333056},
    {'ort': 'Gratwein', 'plz': '8111', 'treffpunkt': 'Hauptplatz', 'lat': 47.112778, 'lon': 15.334444},
    {'ort': 'Knittelfeld', 'plz': '8720', 'treffpunkt': 'Hauptplatz', 'lat': 47.215, 'lon': 14.829444},
    {'ort': 'Neunkirchen', 'plz': '2620', 'treffpunkt': 'Hauptplatz', 'lat': 47.726944, 'lon': 16.081667},
    {'ort': 'St. Veit an der Glan', 'plz': '9300', 'treffpunkt': 'Hauptplatz', 'lat': 46.766667, 'lon': 14.360278},
    {'ort': 'Vöcklabruck', 'plz': '4840', 'treffpunkt': 'Stadtplatz', 'lat': 48.008774, 'lon': 13.655315},
    {'ort': 'Lienz', 'plz': '9900', 'treffpunkt': 'Hauptplatz', 'lat': 46.829722, 'lon': 12.769722},
    {'ort': 'Leibnitz', 'plz': '8430', 'treffpunkt': 'Hauptplatz', 'lat': 46.783056, 'lon': 15.545},
    {'ort': 'Enns', 'plz': '4470', 'treffpunkt': 'Hauptplatz', 'lat': 48.216667, 'lon': 14.475},
    {'ort': 'Hollabrunn', 'plz': '2020', 'treffpunkt': 'Hauptplatz', 'lat': 48.5627, 'lon': 16.0807},
    {'ort': 'Rankweil', 'plz': '6830', 'treffpunkt': 'Bahnhofstraße/Ringstraße', 'lat': 47.270557, 'lon': 9.642703},
    {'ort': 'Bad Vöslau', 'plz': '2540', 'treffpunkt': 'Schloßplatz', 'lat': 47.966944, 'lon': 16.214444},
    {'ort': 'Brunn am Gebirge', 'plz': '2345', 'treffpunkt': 'Gemeindeamt', 'lat': 48.1, 'lon': 16.283333},
    {'ort': 'Ried im Innkreis', 'plz': '4910', 'treffpunkt': 'Hauptplatz', 'lat': 48.21, 'lon': 13.489444},
    {'ort': 'Deutschlandsberg', 'plz': '8530', 'treffpunkt': 'Hauptplatz', 'lat': 46.816111, 'lon': 15.215},
    {'ort': 'Weiz', 'plz': '8160', 'treffpunkt': 'Hauptplatz', 'lat': 47.218889, 'lon': 15.625278},
    {'ort': 'Waidhofen an der Ybbs', 'plz': '3340', 'treffpunkt': 'Oberer Stadtplatz', 'lat': 47.966667, 'lon': 14.766667},
    {'ort': 'Mistelbach', 'plz': '2130', 'treffpunkt': 'Hauptplatz', 'lat': 48.566667, 'lon': 16.566667},
    {'ort': 'Götzis', 'plz': '6840', 'treffpunkt': 'Jonas Schlössle', 'lat': 47.333056, 'lon': 9.633333},
    {'ort': 'Trofaiach', 'plz': '8793', 'treffpunkt': 'Hauptstraße', 'lat': 47.426111, 'lon': 15.006667},
    {'ort': 'Gänserndorf', 'plz': '2230', 'treffpunkt': 'Rathausplatz', 'lat': 48.340556, 'lon': 16.7175},
    {'ort': 'Zwettl', 'plz': '3910', 'treffpunkt': 'Hauptplatz', 'lat': 48.603333, 'lon': 15.168889},
    {'ort': 'Völkermarkt', 'plz': '9100', 'treffpunkt': 'Hauptplatz', 'lat': 46.662222, 'lon': 14.634444},
    {'ort': 'St. Johann im Pongau', 'plz': '5600', 'treffpunkt': 'Hauptstraße/Post', 'lat': 47.35, 'lon': 13.2},
    {'ort': 'Gerasdorf bei Wien', 'plz': '2201', 'treffpunkt': 'Rathaus', 'lat': 48.295, 'lon': 16.4675},
    {'ort': 'Seiersberg-Pirka', 'plz': '8054', 'treffpunkt': 'Gemeindeamt', 'lat': 47.01, 'lon': 15.398889},
    {'ort': 'Ebreichsdorf', 'plz': '2442', 'treffpunkt': 'Rathausplatz', 'lat': 47.961111, 'lon': 16.404722},
    {'ort': 'Seekirchen am Wallersee', 'plz': '5201', 'treffpunkt': 'Hauptstraße', 'lat': 47.9, 'lon': 13.133333},
    {'ort': 'Bischofshofen', 'plz': '5500', 'treffpunkt': 'Bahnhofstraße/Sparkasse', 'lat': 47.415609, 'lon': 13.218174},
    {'ort': 'Groß-Enzersdorf', 'plz': '2301', 'treffpunkt': 'Hauptplatz/Stadtsaal', 'lat': 48.201744, 'lon': 16.550551},
    {'ort': 'Gleisdorf', 'plz': '8200', 'treffpunkt': 'Rathausplatz', 'lat': 47.103889, 'lon': 15.708333},
    {'ort': 'Judenburg', 'plz': '8750', 'treffpunkt': 'Hauptplatz', 'lat': 47.1725, 'lon': 14.660278},
    {'ort': 'Imst', 'plz': '6460', 'treffpunkt': 'Johanneskirche', 'lat': 47.239444, 'lon': 10.738056},
    {'ort': 'Köflach', 'plz': '8580', 'treffpunkt': 'Rathausplatz', 'lat': 47.063889, 'lon': 15.088889},
    {'ort': 'St. Andrä', 'plz': '9433', 'treffpunkt': 'Packerstraße/Stadt-Apotheke', 'lat': 46.766667, 'lon': 14.816667},
    {'ort': 'Lauterach', 'plz': '6923', 'treffpunkt': 'Montfortplatz', 'lat': 47.477114, 'lon': 9.731253},
    {'ort': 'Laakirchen', 'plz': '4663', 'treffpunkt': 'Rathausplatz', 'lat': 47.982778, 'lon': 13.824167},
    {'ort': 'Zell am See', 'plz': '5700', 'treffpunkt': 'Stadtplatz', 'lat': 47.323333, 'lon': 12.798056},
    {'ort': 'Purkersdorf', 'plz': '3002', 'treffpunkt': 'Hauptplatz', 'lat': 48.2075, 'lon': 16.175833},
    {'ort': 'Voitsberg', 'plz': '8570', 'treffpunkt': 'Hauptplatz', 'lat': 47.048333, 'lon': 15.150278},
    {'ort': 'St. Valentin', 'plz': '4300', 'treffpunkt': 'Hauptplatz', 'lat': 48.174722, 'lon': 14.533333},
    {'ort': 'Berndorf', 'plz': '2560', 'treffpunkt': 'Rathaus', 'lat': 47.942778, 'lon': 16.103611},
    {'ort': 'Attnang-Puchheim', 'plz': '4800', 'treffpunkt': 'Rathausplatz/Stadtamt', 'lat': 48.01, 'lon': 13.726389},
    {'ort': 'Mürzzuschlag', 'plz': '8680', 'treffpunkt': 'Stadtplatz', 'lat': 47.60639, 'lon': 15.673493},
    {'ort': 'Fürstenfeld', 'plz': '8280', 'treffpunkt': 'Hauptplatz', 'lat': 47.050939, 'lon': 16.076446},
    {'ort': 'Kitzbühel', 'plz': '6370', 'treffpunkt': 'Rathausplatz', 'lat': 47.446389, 'lon': 12.391944},
    {'ort': 'Perg', 'plz': '4320', 'treffpunkt': 'Hauptplatz', 'lat': 48.250278, 'lon': 14.633611},
    {'ort': 'Deutsch-Wagram', 'plz': '2232', 'treffpunkt': 'Marktplatz', 'lat': 48.298203, 'lon': 16.562768},
    {'ort': 'Neulengbach', 'plz': '3040', 'treffpunkt': 'Hauptplatz/Gemeindeamt', 'lat': 48.200278, 'lon': 15.909722},
    {'ort': 'Kindberg', 'plz': '8650', 'treffpunkt': 'Hauptstraße/Post', 'lat': 47.504444, 'lon': 15.448889},
    {'ort': 'Liezen', 'plz': '8940', 'treffpunkt': 'Rathausplatz', 'lat': 47.566667, 'lon': 14.233333},
    {'ort': 'Bruck an der Leitha', 'plz': '2460', 'treffpunkt': 'Hauptplatz', 'lat': 48.0255, 'lon': 16.778972},
    {'ort': 'Neusiedl am See', 'plz': '7100', 'treffpunkt': 'Hauptplatz', 'lat': 47.948611, 'lon': 16.843056},
    {'ort': 'Landeck', 'plz': '6500', 'treffpunkt': 'Malserstraße/Innstraße', 'lat': 47.137214, 'lon': 10.566864},
    {'ort': 'Herzogenburg', 'plz': '3130', 'treffpunkt': 'Rathausplatz', 'lat': 48.286111, 'lon': 15.696389},
    {'ort': 'Freistadt', 'plz': '4240', 'treffpunkt': 'Hauptplatz', 'lat': 48.511667, 'lon': 14.506111},
    {'ort': 'Langenlois', 'plz': '3550', 'treffpunkt': 'Holzplatz/Post', 'lat': 48.473096, 'lon': 15.676083},
    {'ort': 'Fehring', 'plz': '8350', 'treffpunkt': 'Hauptplatz/Post', 'lat': 46.936389, 'lon': 16.010556},
    {'ort': 'Oberwart', 'plz': '7400', 'treffpunkt': 'Hauptplatz', 'lat': 47.287778, 'lon': 16.203056},
    {'ort': 'Zeltweg', 'plz': '8740', 'treffpunkt': 'Hauptplatz', 'lat': 47.190556, 'lon': 14.751111},
    {'ort': 'Pressbaum', 'plz': '3021', 'treffpunkt': 'Hauptstraße/Rathaus', 'lat': 48.178889, 'lon': 16.0775},
    {'ort': 'Mattersburg', 'plz': '7210', 'treffpunkt': 'Hauptplatz', 'lat': 47.736947, 'lon': 16.397691},
    {'ort': 'Ferlach', 'plz': '9170', 'treffpunkt': 'Hauptplatz', 'lat': 46.526533, 'lon': 14.300629},
    {'ort': 'Wolkersdorf', 'plz': '2120', 'treffpunkt': 'Rathaus', 'lat': 48.383056, 'lon': 16.518056},
    {'ort': 'Hermagor', 'plz': '9620', 'treffpunkt': 'Gasserplatz', 'lat': 46.627499, 'lon': 13.371195},
    {'ort': 'Schladming', 'plz': '8970', 'treffpunkt': 'Hauptplatz', 'lat': 47.391762, 'lon': 13.688908},
    {'ort': 'Frohnleiten', 'plz': '8130', 'treffpunkt': 'Hauptplatz', 'lat': 47.270278, 'lon': 15.324444},
    {'ort': 'Horn', 'plz': '3580', 'treffpunkt': 'Rathausplatz', 'lat': 48.663889, 'lon': 15.657221999999999},
    {'ort': 'Hartberg', 'plz': '8230', 'treffpunkt': 'Hauptplatz', 'lat': 47.280556, 'lon': 15.97},
    {'ort': 'Wilhelmsburg', 'plz': '3150', 'treffpunkt': 'Hauptplatz', 'lat': 48.110833, 'lon': 15.61},
    {'ort': 'Hainburg', 'plz': '2410', 'treffpunkt': 'Hauptplatz', 'lat': 48.147778, 'lon': 16.941944},
    {'ort': 'Gallneukirchen', 'plz': '4210', 'treffpunkt': 'Marktplatz/Brunnen', 'lat': 48.352748, 'lon': 14.416691},
    {'ort': 'Laa an der Thaya', 'plz': '2136', 'treffpunkt': 'Stadtplatz', 'lat': 48.7225, 'lon': 16.386667},
    {'ort': 'Neumarkt am Wallersee', 'plz': '5202', 'treffpunkt': 'Hauptstraße/Gemeindeamt', 'lat': 47.945278, 'lon': 13.224722},
    {'ort': 'Mattighofen', 'plz': '5230', 'treffpunkt': 'Stadtplatz', 'lat': 48.106667, 'lon': 13.149444},
    {'ort': 'Traismauer', 'plz': '3133', 'treffpunkt': 'Hauptplatz', 'lat': 48.333333, 'lon': 15.733056},
    {'ort': 'Gloggnitz', 'plz': '2640', 'treffpunkt': 'Sparkassenplatz', 'lat': 47.675833, 'lon': 15.938333},
    {'ort': 'Radenthein', 'plz': '9545', 'treffpunkt': 'Hauptstraße/Mirnockstraße', 'lat': 46.801082, 'lon': 13.705142},
    {'ort': 'Bärnbach', 'plz': '8572', 'treffpunkt': 'Hauptplatz', 'lat': 47.070778, 'lon': 15.128186},
    {'ort': 'Ybbs', 'plz': '3370', 'treffpunkt': 'Hauptplatz', 'lat': 48.166667, 'lon': 15.066667},
    {'ort': 'Pinkafeld', 'plz': '7423', 'treffpunkt': 'Hauptplatz', 'lat': 47.371667, 'lon': 16.121944},
    {'ort': 'Waidhofen an der Thaya', 'plz': '3830', 'treffpunkt': 'Hauptplatz', 'lat': 48.816667, 'lon': 15.283333},
    {'ort': 'Oberndorf bei Salzburg', 'plz': '5110', 'treffpunkt': 'Salzbuger Straße/Joseph-Mohr-Straße', 'lat': 47.943604, 'lon': 12.942449},
    {'ort': 'Poysdorf', 'plz': '2170', 'treffpunkt': 'Weinmarktplatz', 'lat': 48.669374, 'lon': 16.630012},
    {'ort': 'Gmünd', 'plz': '3950', 'treffpunkt': 'Stadtplatz', 'lat': 48.773172, 'lon': 14.983214},
    {'ort': 'Stadt Haag', 'plz': '3350', 'treffpunkt': 'Hauptplatz', 'lat': 48.112222, 'lon': 14.565556},
    {'ort': 'Schrems', 'plz': '3943', 'treffpunkt': 'Hauptplatz', 'lat': 48.783333, 'lon': 15.066667},
    {'ort': 'Mittersill', 'plz': '5730', 'treffpunkt': 'Stadtplatz', 'lat': 47.266667, 'lon': 12.466667},
    {'ort': 'Zistersdorf', 'plz': '2225', 'treffpunkt': 'Hauptstraße/Dreifaltigkeitsgasse', 'lat': 48.545489, 'lon': 16.762762},
    {'ort': 'Fischamend', 'plz': '2401', 'treffpunkt': 'Hauptplatz', 'lat': 48.118901, 'lon': 16.61134},
    {'ort': 'Melk', 'plz': '3390', 'treffpunkt': 'Rathausplatz', 'lat': 48.226944, 'lon': 15.343889},
    {'ort': 'Spielberg', 'plz': '8724', 'treffpunkt': 'Marktplatz/Sparkasse', 'lat': 47.208008, 'lon': 14.796445},
    {'ort': 'Pregarten', 'plz': '4230', 'treffpunkt': 'Stadtplatz', 'lat': 48.355556, 'lon': 14.530556},
    {'ort': 'Rottenmann', 'plz': '8786', 'treffpunkt': 'Stadtgemeindeamt', 'lat': 47.525546, 'lon': 14.358132},
    {'ort': 'Rohrbach', 'plz': '4150', 'treffpunkt': 'Stadtplatz', 'lat': 48.573333, 'lon': 13.991667},
    {'ort': 'Bad Hall', 'plz': '4540', 'treffpunkt': 'Hauptplatz', 'lat': 48.033333, 'lon': 14.2},
    {'ort': 'Steyregg', 'plz': '4221', 'treffpunkt': 'Stadtplatz', 'lat': 48.285817, 'lon': 14.371903},
    {'ort': 'Friesach', 'plz': '9360', 'treffpunkt': 'Hauptplatz', 'lat': 46.950645, 'lon': 14.405945},
    {'ort': 'Schärding', 'plz': '4780', 'treffpunkt': 'Oberer Stadtplatz', 'lat': 48.456944, 'lon': 13.431667},
    {'ort': 'Radstadt', 'plz': '5550', 'treffpunkt': 'Stadtplatz', 'lat': 47.383333, 'lon': 13.466667},
    {'ort': 'Grieskirchen', 'plz': '4710', 'treffpunkt': 'Stadtplatz', 'lat': 48.235, 'lon': 13.831944},
    {'ort': 'Altheim', 'plz': '4950', 'treffpunkt': 'Stadtplatz', 'lat': 48.250257, 'lon': 13.232625},
    {'ort': 'Althofen', 'plz': '9330', 'treffpunkt': 'Hauptplatz', 'lat': 46.866667, 'lon': 14.466667},
    {'ort': 'Bad Aussee', 'plz': '8990', 'treffpunkt': 'Kurhausplatz', 'lat': 47.609438, 'lon': 13.783382},
    {'ort': 'Retz', 'plz': '2070', 'treffpunkt': 'Hauptplatz', 'lat': 48.756111, 'lon': 15.952222},
    {'ort': 'Schwanenstadt', 'plz': '4690', 'treffpunkt': 'Sparkassenplatz', 'lat': 48.055369, 'lon': 13.775557},
    {'ort': 'Scheibbs', 'plz': '3270', 'treffpunkt': 'Hauptstraße/Gaminger Straße', 'lat': 48.006274, 'lon': 15.16663},
    {'ort': 'Mariazell', 'plz': '8630', 'treffpunkt': 'Hauptplatz', 'lat': 47.773063, 'lon': 15.317687},
    {'ort': 'Lilienfeld', 'plz': '3180', 'treffpunkt': 'Gemeindeamt', 'lat': 48.014881, 'lon': 15.594985},
    {
      "ort": "Favoriten",
      "plz": "1100",
      "treffpunkt": "Reumannplatz",
      "lat": 48.1742612,
      "lon": 16.378051
    },
    {
      "ort": "Simmering",
      "plz": "1110",
      "treffpunkt": "Simmeringer Platz",
      "lat": 48.1700213,
      "lon": 16.420356
    },
    {
      "ort": "Meidling",
      "plz": "1120",
      "treffpunkt": "Meidlinger Hauptstraße",
      "lat": 48.174553,
      "lon": 16.330512
    },
    {
      "ort": "Innere Stadt",
      "plz": "1010",
      "treffpunkt": "Schottentor",
      "lat": 48.213891,
      "lon": 16.362456
    },
    {
      "ort": "Penzing",
      "plz": "1140",
      "treffpunkt": "Hütteldorferstraße",
      "lat": 48.199085,
      "lon": 16.313013
    },
    {
      "ort": "Rudolfsheim-Fünfhaus",
      "plz": "1150",
      "treffpunkt": "Urban-Loritz-Platz",
      "lat": 48.20182,
      "lon": 16.337309
    },
    {
      "ort": "Neubau",
      "plz": "1070",
      "treffpunkt": "Westahnhof",
      "lat": 48.196792,
      "lon": 16.338354
    },
    {
      "ort": "Ottakring",
      "plz": "1160",
      "treffpunkt": "U-Bahnstation Ottakring",
      "lat": 48.212524,
      "lon": 16.311716
    },
    {
      "ort": "Floridsdorf",
      "plz": "1210",
      "treffpunkt": "Franz-Jonas-Platz",
      "lat": 48.256535,
      "lon": 16.398953
    },
    {
      "ort": "Donaustadt",
      "plz": "1220",
      "treffpunkt": "Kagran",
      "lat": 48.243137,
      "lon": 16.433665
    },
    {
      "ort": "Liesing",
      "plz": "1230",
      "treffpunkt": "Siebenhirten",
      "lat": 48.129801,
      "lon": 16.30994
    },
    {
      "ort": "Linz",
      "plz": "4020",
      "treffpunkt": "Hauptbahnhof",
      "lat": 48.291651,
      "lon": 14.291064
    },
    {
      "ort": "Salzburg",
      "plz": "5020",
      "treffpunkt": "Südtiroler Platz",
      "lat": 47.813435,
      "lon": 13.043762
    },
    {
      "ort": "Graz",
      "plz": "8020",
      "treffpunkt": "Europaplatz / Hauptbahnhof",
      "lat": 47.07295,
      "lon": 15.417777
    },
    {
      "ort": "Klagenfurt",
      "plz": "9020",
      "treffpunkt": "Walther-von-der-Vogelweide-Platz",
      "lat": 46.6163467,
      "lon": 14.313621
    },
    {
      "ort": "Innsbruck",
      "plz": "6020",
      "treffpunkt": "Südtiroler Platz",
      "lat": 47.263753,
      "lon": 11.399986
    }
]
