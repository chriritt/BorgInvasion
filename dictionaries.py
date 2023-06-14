
# ship rooms, directions and contents
locations = {
    'bridge': {
        'name': 'on the bridge',
        'east': 'ready room',
        'north': 'observation lounge',
        'equipment': []},

    'ready room': {
        'name': 'in the captain\'s ready room',
        'west': 'bridge',
        'equipment': ['tricorder']},

    'observation lounge': {
        'name': 'in the observation lounge',
        'north': 'armory',
        'south': 'bridge',
        'equipment': ['shield']},

    'armory': {
        'name': 'in the armory',
        'east': 'turbo lift',
        'south': 'observation lounge',
        'south east': 'turbo lift',
        'equipment': ['phaser']},

    'sick bay': {
        'name': 'in sick bay',
        'west': 'turbo lift',
        'north': 'science lab',
        'equipment': ['medkit']},

    'science lab': {
        'name': 'in the science lab',
        'west': 'crew quarters',
        'south': 'sick bay',
        'equipment': ['phase-adapter']},

    'crew quarters': {
        'name': 'in your quarters',
        'east': 'science lab',
        'north': 'turbo lift 2',
        'equipment': ['bat\'leth']},

    'engineering': {
        'name': 'in engineering',
        'south east': 'turbo lift',
        'equipment': []},

    'turbo lift': {
        'name': 'on the turbo lift',
        'west': 'armory',
        'east': 'sick bay',
        'equipment': []},
    
     'turbo lift 2': {
        'name': 'on the turbo lift',
        'south': 'crew quarters',
        'north': 'engineering', 
        'equipment': []}
}

story = {
    'backstory': {
        'During a routine mission, the USS Enterprise-D unexpectedly encountered a formidable Borg cube. \nDespite valiant efforts, the Borg overwhelmed the ship\'s defenses, leaving most of the crew incapacitated. \nIn the midst of the chaos, Worf fought courageously, engaging multiple Borg drones in intense combat. \nHowever, he was eventually struck down and rendered unconscious by a powerful blast from an assimilation tubule. \nNow, as Worf awakens on the bridge, he finds himself surrounded by the aftermath of the Borg assault, his crewmates lying motionless. \nDetermined to assess the situation and protect the ship, Worf\'s warrior instincts kick in as he searches for any signs of the Borg presence and a possible way to regain control of the USS Enterprise...'},

    'ending': 
        {"In the heart of Engineering, Worf assesses the dire situation. \nThe Borg, their shields rapidly adapting to conventional weapons, pose a formidable threat. Remembering the phase adapter he acquired, he swiftly connects it to the ship's main control panel, initiating a pulse that disrupts the Borg's shield adaptations. \nAs the Borg drones falter, their defenses momentarily compromised, Worf seizes the opportunity. \nWith strategic precision, he engages in a relentless assault, utilizing his bat'leth and phaser to incapacitate the remaining drones. \nWith the Borg threat neutralized, Worf proceeds to reactivate critical systems and restore control to the Enterprise. \nHe swiftly coordinates with the remaining crew members, freeing them from their assimilation chambers and providing medical aid to the injured. Worf's unwavering determination and resourcefulness in utilizing the phase adapter proved decisive in saving the Enterprise and his fellow crewmates from the clutches of the Borg. \nThe ship returns to its rightful state, the crew grateful for Worf's heroic actions, and their collective spirit unbroken by the assimilation attempt. \nThrough his bravery and strategic thinking, Worf emerges victorious, proving once again the indomitable spirit of a Klingon warrior in the face of adversity."}
}