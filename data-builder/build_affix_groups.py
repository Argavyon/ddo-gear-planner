from write_json import write_json

from typedefs import AffixGroup

def build_affix_groups() -> None:
    all_saves = ['Fortitude Save', 'Reflex Save', 'Will Save']
    all_skills = ['Balance', 'Bluff', 'Concentration', 'Diplomacy', 'Disable Device', 'Fortitude Save', 'Spot', 'Haggle', 'Heal', 'Hide', 'Intimidate', 'Jump', 'Listen', 'Move Silently', 'Open Lock', 'Perform', 'Reflex Save', 'Repair', 'Resistance', 'Search', 'Spellcraft', 'Spot', 'Swim', 'Tumble', 'Will Save', 'Use Magic Device']

    groups: list[AffixGroup] = [
        # Technically Armor/Weapon Enhancement Bonuses add to AC / Accuracy & Deadly, but we'd need to fake a channel for them
        # and I don't really care about them.
        # AffixGroup(name = 'Enhancement Bonus (Armor)', affixes = ['Armor Class']),
        # AffixGroup(name = 'Enhancement Bonus (Weapon)', affixes = ['Accuracy', 'Deadly']),
        AffixGroup(name = 'Resistance', affixes = all_saves),
        AffixGroup(name = 'Good Luck', affixes = ['Resistance', *all_saves, *all_skills]),
        AffixGroup(name = 'Riposte', affixes = ['Armor Class', 'Resistance', *all_saves]),
        AffixGroup(name = 'Parrying', affixes = ['Armor Class', *all_saves]),
        AffixGroup(name = 'Sheltering', affixes = ['Physical Sheltering', 'Magical Sheltering']),
        AffixGroup(name = 'Well Rounded', affixes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']),
        AffixGroup(name = 'Combat Mastery', affixes = ['Vertigo', 'Stunning', 'Dazing', 'Sundering', 'Shatter']),
        AffixGroup(name = 'each Amplification', affixes = ['Healing Amplification', 'Negative Amplification', 'Repair Amplification']),

        # special case exists where Litany of the Dead Ability Bonus is really well rounded affix
        # but we treat as an affix group to keep consistency with Litany of the Dead Combat Bonus affix
        AffixGroup(name = 'Litany of the Dead - Ability Bonus', affixes = ['Well Rounded']),
        AffixGroup(name = 'Litany of the Dead II - Ability Bonus', affixes = ['Well Rounded']),
        AffixGroup(name = 'Litany of the Dead - Combat Bonus', affixes = ['Accuracy', 'Deadly']),
        AffixGroup(name = 'Litany of the Dead II - Combat Bonus', affixes = ['Accuracy', 'Deadly']),

        # Spells
        AffixGroup(name = 'Potency', affixes = ['Corrosion', 'Combustion', 'Glaciation', 'Magnetism', 'Resonance', 'Impulse', 'Radiance', 'Devotion', 'Nullification', 'Reconstruction']),
        AffixGroup(name = 'Spell Lore', affixes = ['Acid Lore', 'Fire Lore', 'Ice Lore', 'Lightning Lore', 'Sonic Lore', 'Kinetic Lore', 'Radiance Lore', 'Healing Lore', 'Void Lore', 'Repair Lore']),
        AffixGroup(name = 'Negative and Poison Spell Crit Damage', affixes = ['Negative Spell Crit Damage', 'Poison Spell Crit Damage']),
        AffixGroup(name = 'Power of the Frozen Storm', affixes = ['Glaciation', 'Magnetism']),
        AffixGroup(name = 'Power of the Frozen Depths', affixes = ['Glaciation', 'Nullification']),
        AffixGroup(name = 'Power of the Flames of Purity', affixes = ['Combustion', 'Radiance']),
        AffixGroup(name = 'Power of the Silver Flame', affixes = ['Devotion', 'Radiance']),
        AffixGroup(name = 'Frozen Depths Lore', affixes = ['Ice Lore', 'Void Lore']),
        AffixGroup(name = 'Frozen Storm Lore', affixes = ['Ice Lore', 'Lightning Lore']),
        AffixGroup(name = 'Purifying Flame Lore', affixes = ['Fire Lore', 'Radiance Lore']),
        AffixGroup(name = 'Spell Focus Mastery', affixes = ['Evocation Focus', 'Necromancy Focus', 'Transmutation Focus', 'Enchantment Focus', 'Conjuration Focus', 'Abjuration Focus', 'Illusion Focus']),

        # Skills
        AffixGroup(name = 'Alluring Skills Bonus', affixes = ['Bluff', 'Diplomacy', 'Haggle', 'Intimidate', 'Perform']),
        AffixGroup(name = 'Charisma Skills', affixes = ['Bluff', 'Diplomacy', 'Haggle', 'Intimidate', 'Perform']),
        AffixGroup(name = 'Intelligence Skills', affixes = ['Disable Device', 'Repair', 'Search', 'Spellcraft']),
        AffixGroup(name = 'Dexterity Skills', affixes = ['Balance', 'Hide', 'Move Silently', 'Open Locks', 'Tumble']),
        AffixGroup(name = 'Strength Skills', affixes = ['Jump']),
        AffixGroup(name = 'Wisdom Skills', affixes = ['Heal', 'Listen', 'Spot']),
        AffixGroup(name = 'Constitution Skills', affixes = ['Concentration']),
    ]

    write_json(groups, 'affix-groups')


if __name__ == "__main__":
    build_affix_groups()