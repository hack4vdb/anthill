#!/usr/bin/python
# -*- coding: utf-8 -*-

wahl_details = [
    {
        'ort': 'Villach',
        'wg1_hofer': 0.397,
        'wg1_vdb': 0.1601,
        'wg2_hofer': 0.5618,
        'wg2_vdb': 0.4382,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wels',
        'wg1_hofer': 0.4048,
        'wg1_vdb': 0.215,
        'wg2_hofer': 0.495,
        'wg2_vdb': 0.505,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'St. Pölten',
        'wg1_hofer': 0.3181,
        'wg1_vdb': 0.2238,
        'wg2_hofer': 0.4527,
        'wg2_vdb': 0.5473,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Dornbirn',
        'wg1_hofer': 0.3039,
        'wg1_vdb': 0.2991,
        'wg2_hofer': 0.4195,
        'wg2_vdb': 0.5805,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wiener Neustadt',
        'wg1_hofer': 0.3858,
        'wg1_vdb': 0.2139,
        'wg2_hofer': 0.5069,
        'wg2_vdb': 0.4931,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Steyr',
        'wg1_hofer': 0.357,
        'wg1_vdb': 0.2169,
        'wg2_hofer': 0.4724,
        'wg2_vdb': 0.5276,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Feldkirch',
        'wg1_hofer': 0.2968,
        'wg1_vdb': 0.3222,
        'wg2_hofer': 0.4044,
        'wg2_vdb': 0.5956,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bregenz',
        'wg1_hofer': 0.2957,
        'wg1_vdb': 0.3092,
        'wg2_hofer': 0.4056,
        'wg2_vdb': 0.5944,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Leonding',
        'wg1_hofer': 0.3174,
        'wg1_vdb': 0.258,
        'wg2_hofer': 0.4242,
        'wg2_vdb': 0.5758,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Klosterneuburg',
        'wg1_hofer': 0.2351,
        'wg1_vdb': 0.3038,
        'wg2_hofer': 0.3563,
        'wg2_vdb': 0.6437,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Baden',
        'wg1_hofer': 0.2865,
        'wg1_vdb': 0.2715,
        'wg2_hofer': 0.4207,
        'wg2_vdb': 0.5793,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Leoben',
        'wg1_hofer': 0.4307,
        'wg1_vdb': 0.1509,
        'wg2_hofer': 0.5868,
        'wg2_vdb': 0.4132,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wolfsberg',
        'wg1_hofer': 0.4361,
        'wg1_vdb': 0.1117,
        'wg2_hofer': 0.658,
        'wg2_vdb': 0.342,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Krems an der Donau',
        'wg1_hofer': 0.3438,
        'wg1_vdb': 0.2154,
        'wg2_hofer': 0.4839,
        'wg2_vdb': 0.5161,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Traun',
        'wg1_hofer': 0.3919,
        'wg1_vdb': 0.1964,
        'wg2_hofer': 0.4896,
        'wg2_vdb': 0.5104,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Amstetten',
        'wg1_hofer': 0.3816,
        'wg1_vdb': 0.1855,
        'wg2_hofer': 0.5299,
        'wg2_vdb': 0.4701,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Kapfenberg',
        'wg1_hofer': 0.446,
        'wg1_vdb': 0.1272,
        'wg2_hofer': 0.5925,
        'wg2_vdb': 0.4075,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Lustenau',
        'wg1_hofer': 0.3522,
        'wg1_vdb': 0.2668,
        'wg2_hofer': 0.4516,
        'wg2_vdb': 0.5484,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hallein',
        'wg1_hofer': 0.3885,
        'wg1_vdb': 0.2158,
        'wg2_hofer': 0.5001,
        'wg2_vdb': 0.4999,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Mödling',
        'wg1_hofer': 0.2348,
        'wg1_vdb': 0.3096,
        'wg2_hofer': 0.3622,
        'wg2_vdb': 0.6378,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Kufstein',
        'wg1_hofer': 0.3815,
        'wg1_vdb': 0.2502,
        'wg2_hofer': 0.4887,
        'wg2_vdb': 0.5113,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Traiskirchen',
        'wg1_hofer': 0.4076,
        'wg1_vdb': 0.202,
        'wg2_hofer': 0.537,
        'wg2_vdb': 0.463,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Schwechat',
        'wg1_hofer': 0.4097,
        'wg1_vdb': 0.1962,
        'wg2_hofer': 0.5375,
        'wg2_vdb': 0.4625,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Braunau am Inn',
        'wg1_hofer': 0.3924,
        'wg1_vdb': 0.2044,
        'wg2_hofer': 0.5314,
        'wg2_vdb': 0.4686,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Stockerau',
        'wg1_hofer': 0.3558,
        'wg1_vdb': 0.2045,
        'wg2_hofer': 0.4918,
        'wg2_vdb': 0.5082,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Saalfelden am Steinernen Meer',
        'wg1_hofer': 0.3947,
        'wg1_vdb': 0.1777,
        'wg2_hofer': 0.556,
        'wg2_vdb': 0.444,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Tulln',
        'wg1_hofer': 0.3502,
        'wg1_vdb': 0.1874,
        'wg2_hofer': 0.5208,
        'wg2_vdb': 0.4792,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ansfelden',
        'wg1_hofer': 0.4355,
        'wg1_vdb': 0.1738,
        'wg2_hofer': 0.5464,
        'wg2_vdb': 0.4536,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hohenems',
        'wg1_hofer': 0.3819,
        'wg1_vdb': 0.2664,
        'wg2_hofer': 0.5033,
        'wg2_vdb': 0.4967,
        'wenigwahler': True,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Bruck an der Mur',
        'wg1_hofer': 0.4092,
        'wg1_vdb': 0.156,
        'wg2_hofer': 0.5649,
        'wg2_vdb': 0.4351,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Spittal an der Drau',
        'wg1_hofer': 0.407,
        'wg1_vdb': 0.1309,
        'wg2_hofer': 0.5989,
        'wg2_vdb': 0.4011,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Telfs',
        'wg1_hofer': 0.3696,
        'wg1_vdb': 0.2774,
        'wg2_hofer': 0.4815,
        'wg2_vdb': 0.5185,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Perchtoldsdorf',
        'wg1_hofer': 0.2432,
        'wg1_vdb': 0.2849,
        'wg2_hofer': 0.3724,
        'wg2_vdb': 0.6276,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ternitz',
        'wg1_hofer': 0.421,
        'wg1_vdb': 0.1607,
        'wg2_hofer': 0.5655,
        'wg2_vdb': 0.4345,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Eisenstadt',
        'wg1_hofer': 0.3618,
        'wg1_vdb': 0.2092,
        'wg2_hofer': 0.5126,
        'wg2_vdb': 0.4874,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Feldkirchen',
        'wg1_hofer': 0.4269,
        'wg1_vdb': 0.1135,
        'wg2_hofer': 0.6464,
        'wg2_vdb': 0.3536,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bludenz',
        'wg1_hofer': 0.3262,
        'wg1_vdb': 0.2695,
        'wg2_hofer': 0.4245,
        'wg2_vdb': 0.5755,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bad Ischl',
        'wg1_hofer': 0.3288,
        'wg1_vdb': 0.2303,
        'wg2_hofer': 0.4527,
        'wg2_vdb': 0.5473,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hall in Tirol',
        'wg1_hofer': 0.3281,
        'wg1_vdb': 0.2905,
        'wg2_hofer': 0.4304,
        'wg2_vdb': 0.5696,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Schwaz',
        'wg1_hofer': 0.3785,
        'wg1_vdb': 0.2482,
        'wg2_hofer': 0.5186,
        'wg2_vdb': 0.4814,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Feldbach',
        'wg1_hofer': 0.417,
        'wg1_vdb': 0.1295,
        'wg2_hofer': 0.6207,
        'wg2_vdb': 0.3793,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wörgl',
        'wg1_hofer': 0.4067,
        'wg1_vdb': 0.2243,
        'wg2_hofer': 0.5158,
        'wg2_vdb': 0.4842,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wals-Siezenheim',
        'wg1_hofer': 0.4147,
        'wg1_vdb': 0.1933,
        'wg2_hofer': 0.5679,
        'wg2_vdb': 0.4321,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hard',
        'wg1_hofer': 0.3141,
        'wg1_vdb': 0.2932,
        'wg2_hofer': 0.425,
        'wg2_vdb': 0.575,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gmunden',
        'wg1_hofer': 0.3134,
        'wg1_vdb': 0.2598,
        'wg2_hofer': 0.4244,
        'wg2_vdb': 0.5756,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Marchtrenk',
        'wg1_hofer': 0.4563,
        'wg1_vdb': 0.1746,
        'wg2_hofer': 0.5551,
        'wg2_vdb': 0.4449,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Korneuburg',
        'wg1_hofer': 0.3322,
        'wg1_vdb': 0.2437,
        'wg2_hofer': 0.4519,
        'wg2_vdb': 0.5481,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gratwein-Straßengel',
        'wg1_hofer': 0.3892,
        'wg1_vdb': 0.2042,
        'wg2_hofer': 0.534,
        'wg2_vdb': 0.466,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Knittelfeld',
        'wg1_hofer': 0.4225,
        'wg1_vdb': 0.1446,
        'wg2_hofer': 0.5957,
        'wg2_vdb': 0.4043,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Neunkirchen',
        'wg1_hofer': 0.4056,
        'wg1_vdb': 0.189,
        'wg2_hofer': 0.5399,
        'wg2_vdb': 0.4601,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'St. Veit an der Glan',
        'wg1_hofer': 0.402,
        'wg1_vdb': 0.1327,
        'wg2_hofer': 0.5872,
        'wg2_vdb': 0.4128,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Vöcklabruck',
        'wg1_hofer': 0.3275,
        'wg1_vdb': 0.2559,
        'wg2_hofer': 0.4339,
        'wg2_vdb': 0.5661,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Lienz',
        'wg1_hofer': 0.3217,
        'wg1_vdb': 0.2391,
        'wg2_hofer': 0.458,
        'wg2_vdb': 0.542,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Leibnitz',
        'wg1_hofer': 0.4344,
        'wg1_vdb': 0.1531,
        'wg2_hofer': 0.6158,
        'wg2_vdb': 0.3842,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Enns',
        'wg1_hofer': 0.3496,
        'wg1_vdb': 0.198,
        'wg2_hofer': 0.4646,
        'wg2_vdb': 0.5354,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hollabrunn',
        'wg1_hofer': 0.3464,
        'wg1_vdb': 0.1587,
        'wg2_hofer': 0.5541,
        'wg2_vdb': 0.4459,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Rankweil',
        'wg1_hofer': 0.285,
        'wg1_vdb': 0.3139,
        'wg2_hofer': 0.391,
        'wg2_vdb': 0.609,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bad Vöslau',
        'wg1_hofer': 0.3327,
        'wg1_vdb': 0.2546,
        'wg2_hofer': 0.4479,
        'wg2_vdb': 0.5521,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Brunn am Gebirge',
        'wg1_hofer': 0.2801,
        'wg1_vdb': 0.2734,
        'wg2_hofer': 0.3962,
        'wg2_vdb': 0.6038,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ried im Innkreis',
        'wg1_hofer': 0.3648,
        'wg1_vdb': 0.2212,
        'wg2_hofer': 0.4747,
        'wg2_vdb': 0.5253,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Deutschlandsberg',
        'wg1_hofer': 0.3451,
        'wg1_vdb': 0.1374,
        'wg2_hofer': 0.5887,
        'wg2_vdb': 0.4113,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Weiz',
        'wg1_hofer': 0.3379,
        'wg1_vdb': 0.2173,
        'wg2_hofer': 0.4899,
        'wg2_vdb': 0.5101,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Waidhofen an der Ybbs',
        'wg1_hofer': 0.3233,
        'wg1_vdb': 0.1941,
        'wg2_hofer': 0.4859,
        'wg2_vdb': 0.5141,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Mistelbach',
        'wg1_hofer': 0.3687,
        'wg1_vdb': 0.1744,
        'wg2_hofer': 0.5557,
        'wg2_vdb': 0.4443,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Götzis',
        'wg1_hofer': 0.3109,
        'wg1_vdb': 0.3057,
        'wg2_hofer': 0.4322,
        'wg2_vdb': 0.5678,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Trofaiach',
        'wg1_hofer': 0.4439,
        'wg1_vdb': 0.133,
        'wg2_hofer': 0.6105,
        'wg2_vdb': 0.3895,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gänserndorf',
        'wg1_hofer': 0.3956,
        'wg1_vdb': 0.1925,
        'wg2_hofer': 0.5415,
        'wg2_vdb': 0.4585,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Zwettl',
        'wg1_hofer': 0.3709,
        'wg1_vdb': 0.1263,
        'wg2_hofer': 0.6009,
        'wg2_vdb': 0.3991,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Völkermarkt',
        'wg1_hofer': 0.3854,
        'wg1_vdb': 0.1316,
        'wg2_hofer': 0.585,
        'wg2_vdb': 0.415,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gerasdorf bei Wien',
        'wg1_hofer': 0.4087,
        'wg1_vdb': 0.1979,
        'wg2_hofer': 0.5437,
        'wg2_vdb': 0.4563,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Seiersberg-Pirka',
        'wg1_hofer': 0.4083,
        'wg1_vdb': 0.1853,
        'wg2_hofer': 0.5594,
        'wg2_vdb': 0.4406,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ebreichsdorf',
        'wg1_hofer': 0.4385,
        'wg1_vdb': 0.1906,
        'wg2_hofer': 0.57,
        'wg2_vdb': 0.43,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Seekirchen am Wallersee',
        'wg1_hofer': 0.3719,
        'wg1_vdb': 0.2383,
        'wg2_hofer': 0.5186,
        'wg2_vdb': 0.4814,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bischofshofen',
        'wg1_hofer': 0.4143,
        'wg1_vdb': 0.126,
        'wg2_hofer': 0.5998,
        'wg2_vdb': 0.4002,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Groß-Enzersdorf',
        'wg1_hofer': 0.4083,
        'wg1_vdb': 0.1798,
        'wg2_hofer': 0.5519,
        'wg2_vdb': 0.4481,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gleisdorf',
        'wg1_hofer': 0.3842,
        'wg1_vdb': 0.2067,
        'wg2_hofer': 0.5523,
        'wg2_vdb': 0.4477,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Judenburg',
        'wg1_hofer': 0.4429,
        'wg1_vdb': 0.1375,
        'wg2_hofer': 0.6243,
        'wg2_vdb': 0.3757,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Imst',
        'wg1_hofer': 0.4093,
        'wg1_vdb': 0.2616,
        'wg2_hofer': 0.5239,
        'wg2_vdb': 0.4761,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Köflach',
        'wg1_hofer': 0.4887,
        'wg1_vdb': 0.112,
        'wg2_hofer': 0.6603,
        'wg2_vdb': 0.3397,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'St. Andrä',
        'wg1_hofer': 0.4886,
        'wg1_vdb': 0.0742,
        'wg2_hofer': 0.7446,
        'wg2_vdb': 0.2554,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Lauterach',
        'wg1_hofer': 0.3545,
        'wg1_vdb': 0.2562,
        'wg2_hofer': 0.4673,
        'wg2_vdb': 0.5327,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Laakirchen',
        'wg1_hofer': 0.3748,
        'wg1_vdb': 0.1746,
        'wg2_hofer': 0.4936,
        'wg2_vdb': 0.5064,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Zell am See',
        'wg1_hofer': 0.4061,
        'wg1_vdb': 0.1669,
        'wg2_hofer': 0.5699,
        'wg2_vdb': 0.4301,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Purkersdorf',
        'wg1_hofer': 0.2708,
        'wg1_vdb': 0.32,
        'wg2_hofer': 0.3822,
        'wg2_vdb': 0.6178,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Voitsberg',
        'wg1_hofer': 0.4617,
        'wg1_vdb': 0.1279,
        'wg2_hofer': 0.649,
        'wg2_vdb': 0.351,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'St. Valentin',
        'wg1_hofer': 0.3409,
        'wg1_vdb': 0.2067,
        'wg2_hofer': 0.4702,
        'wg2_vdb': 0.5298,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Berndorf',
        'wg1_hofer': 0.4109,
        'wg1_vdb': 0.1915,
        'wg2_hofer': 0.5537,
        'wg2_vdb': 0.4463,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Attnang-Puchheim',
        'wg1_hofer': 0.3805,
        'wg1_vdb': 0.1895,
        'wg2_hofer': 0.4829,
        'wg2_vdb': 0.5171,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Mürzzuschlag',
        'wg1_hofer': 0.3816,
        'wg1_vdb': 0.1565,
        'wg2_hofer': 0.536,
        'wg2_vdb': 0.464,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Fürstenfeld',
        'wg1_hofer': 0.4132,
        'wg1_vdb': 0.1473,
        'wg2_hofer': 0.6008,
        'wg2_vdb': 0.3992,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Kitzbühel',
        'wg1_hofer': 0.3803,
        'wg1_vdb': 0.1982,
        'wg2_hofer': 0.5359,
        'wg2_vdb': 0.4641,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Perg',
        'wg1_hofer': 0.3378,
        'wg1_vdb': 0.187,
        'wg2_hofer': 0.4696,
        'wg2_vdb': 0.5304,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Deutsch-Wagram',
        'wg1_hofer': 0.3964,
        'wg1_vdb': 0.2113,
        'wg2_hofer': 0.5401,
        'wg2_vdb': 0.4599,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Neulengbach',
        'wg1_hofer': 0.3446,
        'wg1_vdb': 0.2299,
        'wg2_hofer': 0.5068,
        'wg2_vdb': 0.4932,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Kindberg',
        'wg1_hofer': 0.3769,
        'wg1_vdb': 0.1214,
        'wg2_hofer': 0.5622,
        'wg2_vdb': 0.4378,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Liezen',
        'wg1_hofer': 0.4075,
        'wg1_vdb': 0.145,
        'wg2_hofer': 0.5924,
        'wg2_vdb': 0.4076,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bruck an der Leitha',
        'wg1_hofer': 0.4015,
        'wg1_vdb': 0.1888,
        'wg2_hofer': 0.5444,
        'wg2_vdb': 0.4556,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Neusiedl am See',
        'wg1_hofer': 0.3557,
        'wg1_vdb': 0.2273,
        'wg2_hofer': 0.509,
        'wg2_vdb': 0.491,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Landeck',
        'wg1_hofer': 0.32,
        'wg1_vdb': 0.2766,
        'wg2_hofer': 0.4154,
        'wg2_vdb': 0.5846,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Herzogenburg',
        'wg1_hofer': 0.3701,
        'wg1_vdb': 0.1791,
        'wg2_hofer': 0.5173,
        'wg2_vdb': 0.4827,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Freistadt',
        'wg1_hofer': 0.3272,
        'wg1_vdb': 0.2304,
        'wg2_hofer': 0.4442,
        'wg2_vdb': 0.5558,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Langenlois',
        'wg1_hofer': 0.3871,
        'wg1_vdb': 0.1864,
        'wg2_hofer': 0.5516,
        'wg2_vdb': 0.4484,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Fehring',
        'wg1_hofer': 0.4546,
        'wg1_vdb': 0.114,
        'wg2_hofer': 0.6679,
        'wg2_vdb': 0.3321,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Oberwart',
        'wg1_hofer': 0.4497,
        'wg1_vdb': 0.1477,
        'wg2_hofer': 0.6079,
        'wg2_vdb': 0.3921,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Zeltweg',
        'wg1_hofer': 0.4815,
        'wg1_vdb': 0.1188,
        'wg2_hofer': 0.6488,
        'wg2_vdb': 0.3512,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Pressbaum',
        'wg1_hofer': 0.2999,
        'wg1_vdb': 0.293,
        'wg2_hofer': 0.4197,
        'wg2_vdb': 0.5803,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Mattersburg',
        'wg1_hofer': 0.4017,
        'wg1_vdb': 0.1904,
        'wg2_hofer': 0.5481,
        'wg2_vdb': 0.4519,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ferlach',
        'wg1_hofer': 0.3851,
        'wg1_vdb': 0.1266,
        'wg2_hofer': 0.5783,
        'wg2_vdb': 0.4217,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wolkersdorf im Weinviertel',
        'wg1_hofer': 0.2694,
        'wg1_vdb': 0.2479,
        'wg2_hofer': 0.426,
        'wg2_vdb': 0.574,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hermagor',
        'wg1_hofer': 0.325,
        'wg1_vdb': 0.1151,
        'wg2_hofer': 0.5441,
        'wg2_vdb': 0.4559,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Schladming',
        'wg1_hofer': 0.4586,
        'wg1_vdb': 0.1273,
        'wg2_hofer': 0.6472,
        'wg2_vdb': 0.3528,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Frohnleiten',
        'wg1_hofer': 0.3844,
        'wg1_vdb': 0.1315,
        'wg2_hofer': 0.5701,
        'wg2_vdb': 0.4299,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Horn',
        'wg1_hofer': 0.3665,
        'wg1_vdb': 0.1652,
        'wg2_hofer': 0.5592,
        'wg2_vdb': 0.4408,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hartberg',
        'wg1_hofer': 0.4191,
        'wg1_vdb': 0.1539,
        'wg2_hofer': 0.6008,
        'wg2_vdb': 0.3992,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Wilhelmsburg',
        'wg1_hofer': 0.3642,
        'wg1_vdb': 0.1759,
        'wg2_hofer': 0.5365,
        'wg2_vdb': 0.4635,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Hainburg a.d. Donau',
        'wg1_hofer': 0.4665,
        'wg1_vdb': 0.1535,
        'wg2_hofer': 0.6267,
        'wg2_vdb': 0.3733,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gallneukirchen',
        'wg1_hofer': 0.2459,
        'wg1_vdb': 0.328,
        'wg2_hofer': 0.3303,
        'wg2_vdb': 0.6697,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Laa an der Thaya',
        'wg1_hofer': 0.3843,
        'wg1_vdb': 0.1278,
        'wg2_hofer': 0.5937,
        'wg2_vdb': 0.4063,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Neumarkt am Wallersee',
        'wg1_hofer': 0.4406,
        'wg1_vdb': 0.191,
        'wg2_hofer': 0.5848,
        'wg2_vdb': 0.4152,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Mattighofen',
        'wg1_hofer': 0.4059,
        'wg1_vdb': 0.1653,
        'wg2_hofer': 0.5905,
        'wg2_vdb': 0.4095,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Traismauer',
        'wg1_hofer': 0.406,
        'wg1_vdb': 0.1691,
        'wg2_hofer': 0.5635,
        'wg2_vdb': 0.4365,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Gloggnitz',
        'wg1_hofer': 0.4249,
        'wg1_vdb': 0.1499,
        'wg2_hofer': 0.5973,
        'wg2_vdb': 0.4027,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Radenthein',
        'wg1_hofer': 0.4257,
        'wg1_vdb': 0.1194,
        'wg2_hofer': 0.6452,
        'wg2_vdb': 0.3548,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bärnbach',
        'wg1_hofer': 0.4884,
        'wg1_vdb': 0.1099,
        'wg2_hofer': 0.646,
        'wg2_vdb': 0.354,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Ybbs an der Donau',
        'wg1_hofer': 0.3633,
        'wg1_vdb': 0.1662,
        'wg2_hofer': 0.5354,
        'wg2_vdb': 0.4646,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Pinkafeld',
        'wg1_hofer': 0.6073,
        'wg1_vdb': 0.1219,
        'wg2_hofer': 0.7302,
        'wg2_vdb': 0.2698,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Waidhofen an der Thaya',
        'wg1_hofer': 0.376,
        'wg1_vdb': 0.1646,
        'wg2_hofer': 0.5564,
        'wg2_vdb': 0.4436,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Oberndorf bei Salzburg',
        'wg1_hofer': 0.3618,
        'wg1_vdb': 0.2398,
        'wg2_hofer': 0.5067,
        'wg2_vdb': 0.4933,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Poysdorf',
        'wg1_hofer': 0.3977,
        'wg1_vdb': 0.0908,
        'wg2_hofer': 0.6385,
        'wg2_vdb': 0.3615,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Gmünd',
        'wg1_hofer': 0.3479,
        'wg1_vdb': 0.1652,
        'wg2_hofer': 0.5143,
        'wg2_vdb': 0.4857,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Haag',
        'wg1_hofer': 0.3195,
        'wg1_vdb': 0.2136,
        'wg2_hofer': 0.4819,
        'wg2_vdb': 0.5181,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Schrems',
        'wg1_hofer': 0.3488,
        'wg1_vdb': 0.1324,
        'wg2_hofer': 0.5523,
        'wg2_vdb': 0.4477,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Mittersill',
        'wg1_hofer': 0.4569,
        'wg1_vdb': 0.1091,
        'wg2_hofer': 0.658,
        'wg2_vdb': 0.342,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Zistersdorf',
        'wg1_hofer': 0.4187,
        'wg1_vdb': 0.1086,
        'wg2_hofer': 0.644,
        'wg2_vdb': 0.356,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Fischamend',
        'wg1_hofer': 0.4302,
        'wg1_vdb': 0.1973,
        'wg2_hofer': 0.5445,
        'wg2_vdb': 0.4555,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Melk',
        'wg1_hofer': 0.3221,
        'wg1_vdb': 0.2086,
        'wg2_hofer': 0.5052,
        'wg2_vdb': 0.4948,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Spielberg',
        'wg1_hofer': 0.4398,
        'wg1_vdb': 0.1234,
        'wg2_hofer': 0.6435,
        'wg2_vdb': 0.3565,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Pregarten',
        'wg1_hofer': 0.3668,
        'wg1_vdb': 0.1898,
        'wg2_hofer': 0.5286,
        'wg2_vdb': 0.4714,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Rottenmann',
        'wg1_hofer': 0.4232,
        'wg1_vdb': 0.1315,
        'wg2_hofer': 0.5876,
        'wg2_vdb': 0.4124,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Rohrbach',
        'wg1_hofer': 0.3339,
        'wg1_vdb': 0.1586,
        'wg2_hofer': 0.5056,
        'wg2_vdb': 0.4944,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': True
    },
    {
        'ort': 'Bad Hall',
        'wg1_hofer': 0.3658,
        'wg1_vdb': 0.1986,
        'wg2_hofer': 0.4962,
        'wg2_vdb': 0.5038,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Steyregg',
        'wg1_hofer': 0.3272,
        'wg1_vdb': 0.2268,
        'wg2_hofer': 0.4469,
        'wg2_vdb': 0.5531,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Friesach',
        'wg1_hofer': 0.4637,
        'wg1_vdb': 0.1073,
        'wg2_hofer': 0.6972,
        'wg2_vdb': 0.3028,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Schärding',
        'wg1_hofer': 0.3823,
        'wg1_vdb': 0.1965,
        'wg2_hofer': 0.4872,
        'wg2_vdb': 0.5128,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Radstadt',
        'wg1_hofer': 0.4621,
        'wg1_vdb': 0.11,
        'wg2_hofer': 0.67,
        'wg2_vdb': 0.33,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Grieskirchen',
        'wg1_hofer': 0.378,
        'wg1_vdb': 0.2262,
        'wg2_hofer': 0.4773,
        'wg2_vdb': 0.5227,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Altheim',
        'wg1_hofer': 0.4483,
        'wg1_vdb': 0.1317,
        'wg2_hofer': 0.632,
        'wg2_vdb': 0.368,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Althofen',
        'wg1_hofer': 0.4266,
        'wg1_vdb': 0.1191,
        'wg2_hofer': 0.6512,
        'wg2_vdb': 0.3488,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Bad Aussee',
        'wg1_hofer': 0.2866,
        'wg1_vdb': 0.2182,
        'wg2_hofer': 0.4467,
        'wg2_vdb': 0.5533,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': False
    },
    {
        'ort': 'Retz',
        'wg1_hofer': 0.3279,
        'wg1_vdb': 0.1522,
        'wg2_hofer': 0.5494,
        'wg2_vdb': 0.4506,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Schwanenstadt',
        'wg1_hofer': 0.3787,
        'wg1_vdb': 0.2109,
        'wg2_hofer': 0.5014,
        'wg2_vdb': 0.4986,
        'wenigwahler': False,
        'swingstate': True,
        'neutral_ground': False
    },
    {
        'ort': 'Scheibbs',
        'wg1_hofer': 0.2449,
        'wg1_vdb': 0.2367,
        'wg2_hofer': 0.4211,
        'wg2_vdb': 0.5789,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Mariazell',
        'wg1_hofer': 0.3532,
        'wg1_vdb': 0.1184,
        'wg2_hofer': 0.5863,
        'wg2_vdb': 0.4137,
        'wenigwahler': True,
        'swingstate': False,
        'neutral_ground': True
    },
    {
        'ort': 'Lilienfeld',
        'wg1_hofer': 0.3223,
        'wg1_vdb': 0.1951,
        'wg2_hofer': 0.497,
        'wg2_vdb': 0.503,
        'wenigwahler': False,
        'swingstate': False,
        'neutral_ground': False
    }
]
