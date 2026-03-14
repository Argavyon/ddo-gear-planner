from write_json import write_json

from typedefs import AffixSynonyms

def build_synonyms() -> None:
    data: list[AffixSynonyms] = [
        AffixSynonyms(name = 'Accuracy', synonyms = ['Attack', 'Hit', 'hit', 'Attack Bonus']),
        AffixSynonyms(name = 'Action Boost Charges', synonyms = ['Action Boost Enhancement']),
        AffixSynonyms(name = 'Arcane Casting Dexterity', synonyms = ['Lesser Arcane Casting Dexterity', 'Greater Arcane Casting Dexterity']),
        AffixSynonyms(name = 'Armor Class', synonyms = ['AC', 'Armor Bonus', 'Natural Armor', 'Natural Armor Bonus', 'Protection', 'Rough Hide', 'Shield', 'Shield Armor Class']),
        # probably want to standardize on 'Armor Piercing' as the name, but re-work needs to be done on cannith crafting to remove drift
        AffixSynonyms(name = 'Armor-Piercing', synonyms = ['Armor Piercing', 'Fortification Bypass', 'Fortification bypass']),
        AffixSynonyms(name = 'Assassinate', synonyms = ['Assassinate DCs']),
        AffixSynonyms(name = 'Deadly', synonyms = ['Damage', 'Damage Bonus']),
        AffixSynonyms(name = 'Devotion', synonyms = ['Positive Spell Power', 'Positive Spellpower']),
        AffixSynonyms(name = 'Evocation Focus', synonyms = ['Evocation Spell DCs']),
        AffixSynonyms(name = 'False Life', synonyms = ['Hit Points', 'Lifeforce', 'Maximum HP', 'Maximum Hit Points', 'maximum hitpoints', 'Vitality', 'your maximum hit points']),
        AffixSynonyms(name = 'Force Spell Crit Damage', synonyms = ['Force and Physical Spell Crit Damage']),
        AffixSynonyms(name = 'Greater Dragonmark Charges', synonyms = ['Greater Dragonmark Enhancement']),
        AffixSynonyms(name = 'Healing Lore', synonyms = ['Positive Spell Crit Chance', 'Positive Spellcrit Chance']),
        AffixSynonyms(name = 'Lesser Dragonmark Charges', synonyms = ['Lesser Dragonmark Enhancement']),
        AffixSynonyms(name = 'Light Spell Crit Damage', synonyms = ['Light and Alignment Spell Crit Damage']),
        AffixSynonyms(name = 'Seeker', synonyms = ['Critical Confirmation and Critical Damage']),
        AffixSynonyms(name = 'Void Lore', synonyms = ['Negative Spell Crit Chance', 'Negative Lore']),
        AffixSynonyms(name = 'Deception', synonyms = ['Sneak Attacks']),
        AffixSynonyms(name = 'Speed', synonyms = ['Striding', 'movement speed']),
        AffixSynonyms(name = 'Physical Sheltering', synonyms = ['Physical Resistance Rating', 'PRR']),
        AffixSynonyms(name = 'Magical Sheltering', synonyms = ['Magical Resistance Rating', 'MRR', 'your Magical Resistance Rating']),
        AffixSynonyms(name = 'Magical Sheltering Cap', synonyms = ['Magical Resistance Rating Cap', 'MRR Cap']),
        AffixSynonyms(name = 'Rage Charges', synonyms = ['Anger', 'Minor Anger']),
        AffixSynonyms(name = 'Sheltering', synonyms = ['Physical and Magical Resistance Rating']),
        AffixSynonyms(name = 'Smite Evil Charges', synonyms = ['Extra Smites']),
        AffixSynonyms(name = 'Spell Focus Mastery', synonyms = ['DCs', 'Spell DCs', 'all Spell DCs', 'all spell DCs', 'Spell DC\'s']),
        AffixSynonyms(name = 'Spell Points', synonyms = ['your maximum Spell Points']),
        AffixSynonyms(name = 'Stunning', synonyms = ['Stunning DCs']),
        AffixSynonyms(name = 'Sunder', synonyms = ['Sunder DCs']),
        AffixSynonyms(name = 'Tactical Abilities', synonyms = ['your Tactical Abilities']),
        AffixSynonyms(name = 'Trip', synonyms = ['Trip DCs']),
        AffixSynonyms(name = 'Universal Spell Power', synonyms = ['Spellcasting Implement', 'Universal Spellpower']),
        AffixSynonyms(name = 'Nullification', synonyms = ['Negative Spell Power']),
        AffixSynonyms(name = 'Healing Amplification', synonyms = ['Positive Healing Amplification', 'Positive Amplification']),
        AffixSynonyms(name = 'Negative Amplification', synonyms = ['Negative Healing Amplification']),
        AffixSynonyms(name = 'Repair Amplification', synonyms = ['Repair Healing Amplification']),
        AffixSynonyms(name = 'Well Rounded', synonyms = ['Ability stats', 'All Ability Scores', 'all Ability Scores', 'all of your Ability Scores', 'each Ability Score', 'Well-Rounded']),
        AffixSynonyms(name = 'Sundering', synonyms = ['Sunder', 'Sunder DC']),
        AffixSynonyms(name = 'Vertigo', synonyms = ['Trip', 'Trip DC']),
        AffixSynonyms(name = 'Silver', synonyms = ['Silver , Alchemical']),
        AffixSynonyms(name = 'Arcane Casting Dexterity', synonyms = ['reduce your Arcane Spell Failure by', 'Arcane Spell Failure']),
    ]

    write_json(data, 'affix-synonyms')


if __name__ == "__main__":
    build_synonyms()
