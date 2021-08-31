import streamlit as st
import compute

st.title('SuperHeroes - Gender-bias in Superhero World')

menu = "Gender Infographic"


st.markdown('''

**Superheroes exist in Gender-biased World.**

Gender bias is a favorite research topic amongst scientists. GPT-3 Researchers found out that gendered bias is
very prominent among model generated texts. More details on original GPT-3 paper : [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), 
[Summary Article](https://medium.com/fair-bytes/how-biased-is-gpt-3-5b2b91f1177). In this Visualization we dive into continous variables in Superheroes dataset
and display surprising bias that we found.
''')

if menu == "Good vs Evil Infographic":
    st.markdown('''
## Good vs. Evil Infographic

Distribution of continuous variables are plotted using KDE and pair-wise plotting.

### Interesting Insights
1. Good Superheroes tend to have **more Power** than Bad superheroes.
2. Bad Superheroes tend to be **more Intelligent** than Good or Neutral Superheroes.
3. Bad and Neutral Superheroes tend to be **more Durable** than Good Superheroes.
4. Bad Superheroes tend to be **heavier** than Good Superheroes.
    ''')
    st.image("./alignment_viz.png")

elif menu == "Gender Infographic":
    st.markdown('''
## Male vs Female Infographic

Distribution of continuous variables are plotted using KDE and pair-wise plotting.
    
### Interesting Insights
1. Male Superheroes tend to be **slightly more Intelligent**(*Bias!*) than Female Superheroes.
2. Male Superheroes tend to be **more Durable**(*Bias!*) than Female Superheroes.
3. Male Superheroes tend to have **more Power**(*Bias!*) than Female Superheroes.
4. Male Superheroes tend to be **heavier and taller** than female Superheroes.
        ''')
    st.image("./gender_viz.png")
elif menu == "ML Prediction":

    st.markdown('''
## ML Prediction

Is your custom Superhero more likely to be Good or Bad? One way to find out!

A 2 layer neural network is trained with loss scheduling in supervised manner. Separate models for Good vs Bad & 
Male vs Female are produced. Loss is managed using one-cycle policy from Leslie N. Smith et al. paper 
[Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](https://arxiv.org/abs/1708.07120). 
The model is then loaded into the Visualization for real-time inference of input parameters. Initial fields are 
pre-populated with Superman data.
    ''')

    pred_type = st.radio("Prediction Type", options=["Alignment", "Gender"], index=0)

    # Height, Weight, Gender, Eye color, Race, Hair color, Publisher, Skin Color, Alignment,
    # Intelligence, Strength, Speed, Durability, Power, Combat
    height = st.number_input("Height (ft)", min_value=0.0, value=6.3)
    weight = st.number_input("Weight (lb)", min_value=0.0, value=225.0)
    if pred_type == "Alignment":
        gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
    eye_color = st.selectbox("Eye color", options=['yellow', 'blue', 'brown', 'white', 'purple', 'black',
       'green', 'red', 'silver', 'grey', 'yellow (without irises)',
       'blue / white', 'hazel', 'green / blue', 'yellow / blue',
       'gold', 'amber', 'violet', 'white / red', 'indigo'], index=1)
    race = st.selectbox("Race", options=['Human', 'Ungaran', 'Mutant', 'Atlantean', 'Alien',
       'God / Eternal', 'Inhuman', 'Metahuman', 'Vampire',
       'Human / Radiation', 'Human-Kree', 'Cyborg', 'Amazon',
       'Human / Cosmic', 'Human / Altered', 'Kakarantharaian',
       'Zen-Whoberian', 'Demon', 'Flora Colossus', 'Human-Vuldarian',
       'Demi-God', 'Symbiote', 'Eternal', 'Bolovaxian', 'Kryptonian',
       'Martian', 'Android', 'Animal', 'Clone', 'Talokite', 'Asgardian',
       'Human-Spartoi', 'Tamaranean', 'Mutant / Clone', 'Frost Giant',
       'Cosmic Entity', 'Neyaphem', 'New God', 'Gorilla', 'Spartoi',
       'Luphomoid', 'Parademon', 'Zombie', 'Bizarro', 'Strontian',
       'Czarnian', 'Korugaran'], index=24)
    hair_color = st.selectbox("Hair color", options=['No Hair', 'Blond', 'Brown', 'Black', 'Orange', 'Pink', 'Red',
       'Auburn', 'Strawberry Blond', 'White', 'Blue', 'Green', 'Magenta',
       'Brown / Black', 'Brown / White', 'blond', 'Silver', 'black',
       'Grey', 'Orange / White', 'Yellow', 'Indigo', 'Purple',
       'Red / White', 'Gold', 'Red / Orange', 'Black / Blue'], index=3)
    publisher = st.selectbox("Publisher", options=['Marvel Comics', 'DC Comics'], index=1)
    skin_color = st.selectbox("Skin color", options=['nan', 'red', 'blue', 'gold', 'green', 'pink', 'silver', 'grey',
       'white', 'orange', 'purple', 'yellow', 'blue-white'], index=0)
    if pred_type == "Gender":
        alignment = st.selectbox("Alignment", options=["good", "bad", "neutral"], index=0)
    stats = st.text_input("Stats (Intelligence,Strength,Speed,Durability,Power,Combat)", value="100,100,100,100,100,85")
    skills = st.multiselect("Skills", default=["Energy Beams"],
                            options=['Element Control', 'Fire Resistance', 'Hyperkinesis', 'Elemental Transmogrification', 'Precognition', 'Banish', 'Nova Force', 'Dexterity', 'Size Changing', 'Agility', 'Spatial Awareness', 'Energy Absorption', 'Energy Beams', 'Levitation', 'Matter Absorption', 'Vision - X-Ray', 'Astral Projection', 'Vision - Telescopic', 'Changing Armor', 'Radiation Immunity', 'Telekinesis', 'Longevity', 'Telepathy Resistance', 'Terrakinesis', 'Possession', 'Animation', 'Animal Oriented Powers', 'Web Creation', 'Weapons Master', 'Vitakinesis', 'Odin Force', 'Sonar', 'Animal Control', 'Power Cosmic', 'Self-Sustenance', 'Peak Human Condition', 'Enhanced Hearing', 'Telepathy', 'Omnilingualism', 'Projection', 'Mind Control Resistance', 'Heat Resistance', 'Energy Blasts', 'Reflexes', 'Power Absorption', 'Vision - Thermal', 'Time Manipulation', 'Omnitrix', 'Magic Resistance', 'Molecular Manipulation', 'Sonic Scream', 'Thirstokinesis', 'Power Nullifier', 'Enhanced Touch', 'Intuitive aptitude', 'Duplication', 'Biokinesis', 'Molecular Dissipation', 'Cold Resistance', 'Vision - Night', 'Toxin and Disease Control', 'Super Strength', 'Invulnerability', 'Molecular Combustion', 'Insanity', 'Power Sense', 'Portal Creation', 'Vision - Microscopic', 'Animal Attributes', 'Technopath/Cyberpath', 'Audio Control', 'Energy Armor', 'Summoning', 'Illumination', 'Cloaking', 'Energy Resistance', 'Radar Sense', 'Dimensional Travel', 'Electrokinesis', 'Vision - Heat', 'Enhanced Sight', 'Energy Manipulation', 'Time Travel', 'Density Control', 'Marksmanship', 'Flight', 'Magic', 'The Force', 'Omnipresent', 'Natural Armor', 'Force Fields', 'Reality Warping', 'Gliding', 'Lantern Power Ring', 'Shapeshifting', 'Enhanced Memory', 'Sub-Mariner', 'Wallcrawling', 'Speed Force', 'Seismic Power', 'Power Augmentation', 'Immortality', 'Mind Blast', 'Gravity Control', 'Radiation Absorption', 'Omniscient', 'Jump', 'Clairvoyance', 'Super Breath', 'Wind Control', 'Probability Manipulation', 'Mind Control', 'Heat Generation', 'Phasing', 'Water Control', 'Astral Travel', 'Symbiote Costume', 'Camouflage', 'Regeneration', 'Dimensional Awareness', 'Stamina', 'Melting', 'Enhanced Smell', 'Stealth', 'Hypnokinesis', 'Anti-Gravity', 'Vision - Cryo', 'Grim Reaping', 'Darkforce Manipulation', 'Illusions', 'Intelligence.1', 'Weapon-based Powers', 'Super Speed', 'Adaptation', 'Weather Control', 'Enhanced Senses', 'Magnetism', 'Toxin and Disease Resistance', 'Energy Constructs', 'Intangibility', 'Invisibility', 'Echolocation', 'Plant Control', 'Phoenix Force', 'Psionic Powers', 'Underwater breathing', 'Empathy', 'Omnipotent', 'Vision - Infrared', 'Cryokinesis', 'Fire Control', 'Photographic Reflexes', 'Accelerated Healing', 'Resurrection', 'Death Touch', 'Hair Manipulation', 'Qwardian Power Ring', 'Durability.1', 'Elasticity', 'Electrical Transport', 'Power Suit', 'Substance Secretion', 'Light Control', 'Danger Sense', 'Teleportation', 'Radiation Control', 'Natural Weapons'])

    pred = st.button(f"Predict {pred_type}")
    if pred:
        if pred_type == "Alignment":
            pred = compute.predict_alignment(height, weight, gender, eye_color, race, hair_color, publisher, skin_color,
                                             stats, skills)
        elif pred_type == "Gender":
            pred = compute.predict_gender(height, weight, alignment, eye_color, race, hair_color, publisher, skin_color,
                                          stats, skills)
        output = st.text(f"Predicted Alignment : {pred[0]}")
        import pandas as pd
        disp = pd.DataFrame(pred[1])
        st.write(disp)

    st.markdown('''
## Model Training

Loss plotted for model training. Loss is managed using one-cycle policy from Leslie N. Smith et al. paper 
[Super-Convergence: Very Fast Training of Neural Networks Using Large Learning Rates](https://arxiv.org/abs/1708.07120).
The trainer is run for 400 epochs with max loss of 5e-5 and weight decay of 1e-3. Early Stopping component is used to
extract checkpoint with lowest validation loss.
        ''')

    st.image("./gender_loss.png")
