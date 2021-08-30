import pickle

import streamlit as st
from fastai.tabular.all import *
import pandas as pd


def load_pandas(fname):
    "Load in a `TabularPandas` object from `fname`"
    res = pickle.load(open(fname, 'rb'))
    return res


@st.cache(allow_output_mutation=True)
def import_preproc(type):
    file = f"{type}_preproc.pkl"
    return load_pandas(file)


@st.cache(allow_output_mutation=True)
def import_model(type):
    file = f"{type}_export.pkl"
    learner = load_learner(file)
    return learner


def parse_stats(stats):
    stat_keys = ["Intelligence", "Strength", "Speed", "Durability", "Power", "Combat"]
    stat_items = stats.split(',')
    assert len(stat_keys) == len(stat_items)
    output = {}
    for i in range(len(stat_keys)):
        output[stat_keys[i]] = float(stat_items[i])
    return output


def one_hot(input, keys):
    output = {}
    for key in keys:
        # Could loop better... :)
        output[key] = key in input
    return output

def parse_pred(type, pred):
    table = pd.DataFrame(pred[2].numpy()).T
    if type == "alignment":
        col_mapping = ["bad", "good", "neutral"]
    elif type == "gender":
        col_mapping = ["Male", "Female"]
    table.columns = col_mapping
    return col_mapping[pred[1]], table

def predict_gender(height, weight, alignment, eye_color, race, hair_color, publisher, skin_color, stats, skills):
    preproc = import_preproc("gender")
    model = import_model("gender")

    dictionary = {'Height (ft)': height, 'Weight (lb)': weight, "Alignment": alignment, "Eye color": eye_color,
                  "Race": race, "Hair color": hair_color, "Publisher": publisher, "Skin color": skin_color,
                  **parse_stats(stats), **one_hot(skills, ['Element Control', 'Fire Resistance', 'Hyperkinesis',
                                                           'Elemental Transmogrification', 'Precognition', 'Banish',
                                                           'Nova Force', 'Dexterity', 'Size Changing', 'Agility',
                                                           'Spatial Awareness', 'Energy Absorption', 'Energy Beams',
                                                           'Levitation', 'Matter Absorption', 'Vision - X-Ray',
                                                           'Astral Projection', 'Vision - Telescopic', 'Changing Armor',
                                                           'Radiation Immunity', 'Telekinesis', 'Longevity',
                                                           'Telepathy Resistance', 'Terrakinesis', 'Possession',
                                                           'Animation', 'Animal Oriented Powers', 'Web Creation',
                                                           'Weapons Master', 'Vitakinesis', 'Odin Force', 'Sonar',
                                                           'Animal Control', 'Power Cosmic', 'Self-Sustenance',
                                                           'Peak Human Condition', 'Enhanced Hearing', 'Telepathy',
                                                           'Omnilingualism', 'Projection', 'Mind Control Resistance',
                                                           'Heat Resistance', 'Energy Blasts', 'Reflexes',
                                                           'Power Absorption', 'Vision - Thermal', 'Time Manipulation',
                                                           'Omnitrix', 'Magic Resistance', 'Molecular Manipulation',
                                                           'Sonic Scream', 'Thirstokinesis', 'Power Nullifier',
                                                           'Enhanced Touch', 'Intuitive aptitude', 'Duplication',
                                                           'Biokinesis', 'Molecular Dissipation', 'Cold Resistance',
                                                           'Vision - Night', 'Toxin and Disease Control',
                                                           'Super Strength', 'Invulnerability', 'Molecular Combustion',
                                                           'Insanity', 'Power Sense', 'Portal Creation',
                                                           'Vision - Microscopic', 'Animal Attributes',
                                                           'Technopath/Cyberpath', 'Audio Control', 'Energy Armor',
                                                           'Summoning', 'Illumination', 'Cloaking', 'Energy Resistance',
                                                           'Radar Sense', 'Dimensional Travel', 'Electrokinesis',
                                                           'Vision - Heat', 'Enhanced Sight', 'Energy Manipulation',
                                                           'Time Travel', 'Density Control', 'Marksmanship', 'Flight',
                                                           'Magic', 'The Force', 'Omnipresent', 'Natural Armor',
                                                           'Force Fields', 'Reality Warping', 'Gliding',
                                                           'Lantern Power Ring', 'Shapeshifting', 'Enhanced Memory',
                                                           'Sub-Mariner', 'Wallcrawling', 'Speed Force',
                                                           'Seismic Power', 'Power Augmentation', 'Immortality',
                                                           'Mind Blast', 'Gravity Control', 'Radiation Absorption',
                                                           'Omniscient', 'Jump', 'Clairvoyance', 'Super Breath',
                                                           'Wind Control', 'Probability Manipulation', 'Mind Control',
                                                           'Heat Generation', 'Phasing', 'Water Control',
                                                           'Astral Travel', 'Symbiote Costume', 'Camouflage',
                                                           'Regeneration', 'Dimensional Awareness', 'Stamina',
                                                           'Melting', 'Enhanced Smell', 'Stealth', 'Hypnokinesis',
                                                           'Anti-Gravity', 'Vision - Cryo', 'Grim Reaping',
                                                           'Darkforce Manipulation', 'Illusions', 'Intelligence.1',
                                                           'Weapon-based Powers', 'Super Speed', 'Adaptation',
                                                           'Weather Control', 'Enhanced Senses', 'Magnetism',
                                                           'Toxin and Disease Resistance', 'Energy Constructs',
                                                           'Intangibility', 'Invisibility', 'Echolocation',
                                                           'Plant Control', 'Phoenix Force', 'Psionic Powers',
                                                           'Underwater breathing', 'Empathy', 'Omnipotent',
                                                           'Vision - Infrared', 'Cryokinesis', 'Fire Control',
                                                           'Photographic Reflexes', 'Accelerated Healing',
                                                           'Resurrection', 'Death Touch', 'Hair Manipulation',
                                                           'Qwardian Power Ring', 'Durability.1', 'Elasticity',
                                                           'Electrical Transport', 'Power Suit', 'Substance Secretion',
                                                           'Light Control', 'Danger Sense', 'Teleportation',
                                                           'Radiation Control', 'Natural Weapons'])
                  }
    input = pd.Series(dictionary).to_frame().T
    print(input)

    to_new = preproc.train.new(input)
    to_new.process()

    return parse_pred("gender", model.predict(to_new.xs.iloc[0]))

def predict_alignment(height, weight, gender, eye_color, race, hair_color, publisher, skin_color, stats, skills):
    preproc = import_preproc("alignment")
    model = import_model("alignment")

    dictionary = {'Height (ft)': height, 'Weight (lb)': weight, "Gender": gender, "Eye color": eye_color,
                  "Race": race, "Hair color": hair_color, "Publisher": publisher, "Skin color": skin_color,
                  **parse_stats(stats), **one_hot(skills, ['Element Control', 'Fire Resistance', 'Hyperkinesis',
                                                           'Elemental Transmogrification', 'Precognition', 'Banish',
                                                           'Nova Force', 'Dexterity', 'Size Changing', 'Agility',
                                                           'Spatial Awareness', 'Energy Absorption', 'Energy Beams',
                                                           'Levitation', 'Matter Absorption', 'Vision - X-Ray',
                                                           'Astral Projection', 'Vision - Telescopic', 'Changing Armor',
                                                           'Radiation Immunity', 'Telekinesis', 'Longevity',
                                                           'Telepathy Resistance', 'Terrakinesis', 'Possession',
                                                           'Animation', 'Animal Oriented Powers', 'Web Creation',
                                                           'Weapons Master', 'Vitakinesis', 'Odin Force', 'Sonar',
                                                           'Animal Control', 'Power Cosmic', 'Self-Sustenance',
                                                           'Peak Human Condition', 'Enhanced Hearing', 'Telepathy',
                                                           'Omnilingualism', 'Projection', 'Mind Control Resistance', 'Heat Resistance', 'Energy Blasts', 'Reflexes', 'Power Absorption', 'Vision - Thermal', 'Time Manipulation', 'Omnitrix', 'Magic Resistance', 'Molecular Manipulation', 'Sonic Scream', 'Thirstokinesis', 'Power Nullifier', 'Enhanced Touch', 'Intuitive aptitude', 'Duplication', 'Biokinesis', 'Molecular Dissipation', 'Cold Resistance', 'Vision - Night', 'Toxin and Disease Control', 'Super Strength', 'Invulnerability', 'Molecular Combustion', 'Insanity', 'Power Sense', 'Portal Creation', 'Vision - Microscopic', 'Animal Attributes', 'Technopath/Cyberpath', 'Audio Control', 'Energy Armor', 'Summoning', 'Illumination', 'Cloaking', 'Energy Resistance', 'Radar Sense', 'Dimensional Travel', 'Electrokinesis', 'Vision - Heat', 'Enhanced Sight', 'Energy Manipulation', 'Time Travel', 'Density Control', 'Marksmanship', 'Flight', 'Magic', 'The Force', 'Omnipresent', 'Natural Armor', 'Force Fields', 'Reality Warping', 'Gliding', 'Lantern Power Ring', 'Shapeshifting', 'Enhanced Memory', 'Sub-Mariner', 'Wallcrawling', 'Speed Force', 'Seismic Power', 'Power Augmentation', 'Immortality', 'Mind Blast', 'Gravity Control', 'Radiation Absorption', 'Omniscient', 'Jump', 'Clairvoyance', 'Super Breath', 'Wind Control', 'Probability Manipulation', 'Mind Control', 'Heat Generation', 'Phasing', 'Water Control', 'Astral Travel', 'Symbiote Costume', 'Camouflage', 'Regeneration', 'Dimensional Awareness', 'Stamina', 'Melting', 'Enhanced Smell', 'Stealth', 'Hypnokinesis', 'Anti-Gravity', 'Vision - Cryo', 'Grim Reaping', 'Darkforce Manipulation', 'Illusions', 'Intelligence.1', 'Weapon-based Powers', 'Super Speed', 'Adaptation', 'Weather Control', 'Enhanced Senses', 'Magnetism', 'Toxin and Disease Resistance', 'Energy Constructs', 'Intangibility', 'Invisibility', 'Echolocation', 'Plant Control', 'Phoenix Force', 'Psionic Powers', 'Underwater breathing', 'Empathy', 'Omnipotent', 'Vision - Infrared', 'Cryokinesis', 'Fire Control', 'Photographic Reflexes', 'Accelerated Healing', 'Resurrection', 'Death Touch', 'Hair Manipulation', 'Qwardian Power Ring', 'Durability.1', 'Elasticity', 'Electrical Transport', 'Power Suit', 'Substance Secretion', 'Light Control', 'Danger Sense', 'Teleportation', 'Radiation Control', 'Natural Weapons'])
                  }
    input = pd.Series(dictionary).to_frame().T
    print(input)

    to_new = preproc.train.new(input)
    to_new.process()

    return parse_pred("alignment", model.predict(to_new.xs.iloc[0]))
