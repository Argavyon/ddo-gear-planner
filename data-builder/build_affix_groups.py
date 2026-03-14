from write_json import write_json

from typedefs import AffixGroup

def get_all_saves(bonusType = None) -> list[str]:
    return ['Fortitude Save', 'Reflex Save', 'Will Save']

def get_all_skills(bonusType = None) -> list[str]:
    return ['Balance', 'Bluff', 'Concentration', 'Diplomacy', 'Disable Device', 'Fortitude Save', 'Spot', 'Haggle', 'Heal', 'Hide', 'Intimidate', 'Jump', 'Listen', 'Move Silently', 'Open Lock', 'Perform', 'Reflex Save', 'Repair', 'Resistance', 'Search', 'Spellcraft', 'Spot', 'Swim', 'Tumble', 'Will Save', 'Use Magic Device']

def build_affix_groups() -> None:
    parrying = get_all_saves()
    parrying.append('Armor Class')

    groups: list[AffixGroup] = [
        # Technically Armor/Weapon Enhancement Bonuses add to AC / Accuracy & Deadly, but we'd need to fake a channel for them
        # and I don't really care about them.
        # AffixGroup(name = 'Enhancement Bonus (Armor)', affixes = ['Armor Class']),
        # AffixGroup(name = 'Enhancement Bonus (Weapon)', affixes = ['Accuracy', 'Deadly']),
        AffixGroup(name = 'Good Luck', affixes = ['Resistance'] + get_all_saves() + get_all_skills()),
        AffixGroup(name = 'Negative and Poison Spell Crit Damage', affixes = ['Negative Spell Crit Damage', 'Poison Spell Crit Damage']),
        AffixGroup(name = 'Resistance', affixes = get_all_saves()),
        AffixGroup(name = 'Riposte', affixes = ['Armor Class', 'Resistance'] + get_all_saves()),
        # special case exists where Litany of the Dead Ability Bonus is really well rounded affix
        # but we treat as an affix group to keep consistency with Litany of the Dead Combat Bonus affix
        AffixGroup(name = 'Litany of the Dead - Ability Bonus', affixes = ['Well Rounded']),
        AffixGroup(name = 'Litany of the Dead II - Ability Bonus', affixes = ['Well Rounded']),
        AffixGroup(name = 'Litany of the Dead - Combat Bonus', affixes = ['Accuracy', 'Deadly']),
        AffixGroup(name = 'Litany of the Dead II - Combat Bonus', affixes = ['Accuracy', 'Deadly']),
        AffixGroup(name = 'Parrying', affixes = parrying),
        AffixGroup(name = 'Sheltering', affixes = ['Physical Sheltering', 'Magical Sheltering']),
        AffixGroup(name = 'Potency', affixes = ['Nullification', 'Radiance', 'Devotion', 'Corrosion', 'Combustion', 'Magnetic', 'Glaciation', 'Reconstruction', 'Impulse', 'Resonance']),
        AffixGroup(name = 'Spell Lore', affixes = ['Nullification Lore', 'Radiance Lore', 'Devotion Lore', 'Corrosion Lore', 'Combustion Lore', 'Magnetic Lore', 'Glaciation Lore', 'Reconstruction Lore', 'Impulse Lore', 'Resonance']),
        AffixGroup(name = 'Combat Mastery', affixes = ['Vertigo', 'Stunning', 'Dazing', 'Sundering', 'Shatter']),
        AffixGroup(name = 'Alluring Skills Bonus', affixes = ['Bluff', 'Diplomacy', 'Haggle', 'Intimidate', 'Perform']),
        AffixGroup(name = 'Charisma Skills', affixes = ['Bluff', 'Diplomacy', 'Haggle', 'Intimidate', 'Perform']),
        AffixGroup(name = 'Frozen Depths Lore', affixes = ['Ice Lore', 'Poison Lore', 'Void Lore']),
        AffixGroup(name = 'Frozen Storm Lore', affixes = ['Ice Lore', 'Lightning Lore']),
        AffixGroup(name = 'Intelligence Skills', affixes = ['Disable Device', 'Repair', 'Search', 'Spellcraft']),
        AffixGroup(name = 'Dexterity Skills', affixes = ['Balance', 'Hide', 'Move Silently', 'Open Locks', 'Tumble']),
        AffixGroup(name = 'Power of the Frozen Storm', affixes = ['Glaciation', 'Magnetism']),
        AffixGroup(name = 'Power of the Frozen Depths', affixes = ['Glaciation', 'Nullification', 'Poison']),
        AffixGroup(name = 'Power of the Flames of Purity', affixes = ['Combustion', 'Radiance']),
        AffixGroup(name = 'Power of the Silver Flame', affixes = ['Devotion', 'Radiance']),
        AffixGroup(name = 'Purifying Flame Lore', affixes = ['Fire Lore', 'Radiance Lore']),
        AffixGroup(name = 'Strength Skills', affixes = ['Jump']),
        AffixGroup(name = 'Wisdom Skills', affixes = ['Heal', 'Listen', 'Spot']),
        AffixGroup(name = 'Constitution Skills', affixes = ['Concentration']),
        AffixGroup(name = 'Well Rounded', affixes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']),
        AffixGroup(name = 'Spell Focus Mastery', affixes = ['Evocation Focus', 'Necromancy Focus', 'Transmutation Focus', 'Enchantment Focus', 'Conjuration Focus', 'Abjuration Focus', 'Illusion Focus']),
        AffixGroup(name = 'each Amplification', affixes = ['Healing Amplification', 'Negative Amplification', 'Repair Amplification']),
    ]

    write_json(groups, 'affix-groups')


if __name__ == "__main__":
    build_affix_groups()