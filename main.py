from human import Human

hosein = Human('Hosein', 'Hojat Ansari')
hosein.organs.eye.set_color('blue')
hosein.organs.head.set_shape('circle')
hosein.personality.set_nationality('Iranian')

hosein.information()

hosein.organs.mouth.say("I'm in love with Programming")
