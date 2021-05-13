from discord import VoiceRegion, VerificationLevel

GUILD_REGIONS = {
    VoiceRegion.amsterdam: ':flag_nl: Amsterdam',
    VoiceRegion.brazil: ':flag_br: Brazil',
    VoiceRegion.dubai: ':flag_ae: Dubai',
    VoiceRegion.eu_central: ':flag_eu: Europe Central',
    VoiceRegion.eu_west: ':flag_eu: Europe West',
    VoiceRegion.europe: ':flag_eu: Europe',
    VoiceRegion.frankfurt: ':flag_de: Frankfurt',
    VoiceRegion.hongkong: ':flag_hk: Hong Kong',
    VoiceRegion.india: ':flag_in: India',
    VoiceRegion.japan: ':flag_jp: Japan',
    VoiceRegion.london: ':flag_gb: London',
    VoiceRegion.russia: ':flag_ru: Russia',
    VoiceRegion.singapore: ':flag_sg: Singapore',
    VoiceRegion.southafrica: ':flag_za: South Africa',
    VoiceRegion.sydney: ':flag_au: Sydney',
    VoiceRegion.us_central: ':flag_us: US Central',
    VoiceRegion.us_east: ':flag_us: US East',
    VoiceRegion.us_south: ':flag_us: US South',
    VoiceRegion.us_west: ':flag_us: US West',
    VoiceRegion.vip_amsterdam: ':flag_nl: VIP Amsterdam',
    VoiceRegion.vip_us_east: ':flag_us: VIP US East',
    VoiceRegion.vip_us_west: ':flag_us: VIP US West'
}

GUILD_VERIFICATION_LEVELS = {
    VerificationLevel.none: 'No verification',
    VerificationLevel.low: 'Low',
    VerificationLevel.medium: 'Medium',
    VerificationLevel.high: 'High',
    VerificationLevel.extreme: 'Extreme'
}