import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#nltk.download('wordnet')
#nltk.download('gutenberg')

text2 = "The town was in flames. The narrow streets leading to the moat and the first terrace belched smoke and " \
       "embers, flames devouring the densely clustered thatched houses and licking at the castle walls. From the " \
       "west, from the harbour gate, the screams and clamour of vicious battle and the dull blows of a battering ram " \
       "smashing against the walls grew ever louder. Their attackers had surrounded them unexpectedly, shattering the " \
       "barricades which had been held by no more than a few soldiers, a handful of townsmen carrying halberds and " \
       "some crossbowmen from the guild. Their horses, decked out in flowing black caparisons, flew over the " \
       "barricades like spectres, their riders’ bright, glistening blades sowing death amongst the fleeing defenders. " \
       "Ciri felt the knight who carried her before him on his saddle abruptly spur his horse. She heard his cry. " \
       "“Hold on,” he shouted. “Hold on!” Other knights wearing the colours of Cintra overtook them, sparring, " \
       "even in full flight, with the Nilfgaardians. Ciri caught a glimpse of the skirmish from the corner of her eye " \
       "– the crazed swirl of blue-gold and black cloaks amidst the clash of steel, the clatter of blades against " \
       "shields, the neighing of horses— Shouts. No, not shouts. Screams. “Hold on!” Fear. With every jolt, " \
       "every jerk, every leap of the horse pain shot through "

text = "The town was in flames. The narrow streets leading to the moat and the first terrace belched smoke and " \
        "embers, flames devouring the densely clustered thatched houses and licking at the castle walls. From the " \
        "west, from the harbour gate, the screams and clamour of vicious battle and the dull blows of a battering ram " \
        "smashing against the walls grew ever louder. Their attackers had surrounded them unexpectedly, shattering " \
        "the barricades which had been held by no more than a few soldiers, a handful of townsmen carrying halberds " \
        "and some crossbowmen from the guild. Their horses, decked out in flowing black caparisons, flew over the " \
        "barricades like spectres, their riders’ bright, glistening blades sowing death amongst the fleeing " \
        "defenders. Ciri felt the knight who carried her before him on his saddle abruptly spur his horse. She heard " \
        "his cry. “Hold on,” he shouted. “Hold on!” Other knights wearing the colours of Cintra overtook them, " \
        "sparring, even in full flight, with the Nilfgaardians. Ciri caught a glimpse of the skirmish from the corner " \
        "of her eye – the crazed swirl of blue-gold and black cloaks amidst the clash of steel, the clatter of blades " \
        "against shields, the neighing of horses— Shouts. No, not shouts. Screams. “Hold on!” Fear. With every jolt, " \
        "every jerk, every leap of the horse pain shot through 5 her hands as she clutched at the reins. Her legs " \
        "contracted painfully, unable to find support, her eyes watered from the smoke. The arm around her suffocated " \
        "her, choking her, the force compressing her ribs. All around her screaming such as she had never before " \
        "heard grew louder. What must one do to a man to make him scream so? Fear. Overpowering, paralysing, " \
        "choking fear. Again the clash of iron, the grunts and snorts of the horses. The houses whirled around her " \
        "and suddenly she could see windows belching fire where a moment before there’d been nothing but a muddy " \
        "little street strewn with corpses and cluttered with the abandoned possessions of the fleeing population. " \
        "All at once the knight at her back was wracked by a strange wheezing cough. Blood spurted over the hands " \
        "grasping the reins. More screams. Arrows whistled past. A fall, a shock, painful bruising against armour. " \
        "Hooves pounded past her, a horse’s belly and a frayed girth flashing by above her head, then another horse’s " \
        "belly and a flowing black caparison. Grunts of exertion, like a lumberjack’s when chopping wood. But this " \
        "isn’t wood; it’s iron against iron. A shout, muffled and dull, and something huge and black collapsed into " \
        "the mud next to her with a splash, spurting blood. An armoured foot quivered, thrashed, goring the earth " \
        "with an enormous spur. A jerk. Some force plucked her up, pulled her onto another saddle. Hold on! Again the " \
        "bone-shaking speed, the mad gallop. Arms and legs desperately searching for support. The horse rears. Hold " \
        "on!… There is no support. There is no… There is no… There is blood. The horse falls. It’s impossible to jump " \
        "aside, no way to break free, to escape the tight embrace of these chainmailclad arms. There is no way to " \
        "avoid the blood pouring onto her head and over her shoulders. A jolt, the squelch of mud, a violent " \
        "collision with the ground, horrifically still after the furious ride. The horse’s harrowing wheezes and " \
        "squeals as it tries to regain its feet. The pounding of horseshoes, fetlocks and hooves flashing past. Black " \
        "caparisons and cloaks. Shouting. The street is on fire, a roaring red wall of flame. Silhouetted before it, " \
        "a rider towers over the flaming roofs, enormous. His black-caparisoned horse prances, tosses its head, " \
        "neighs. The rider stares down at her. Ciri sees his eyes gleaming through the slit in his huge helmet, " \
        "framed by a bird of prey’s wings. She sees the fire reflected in the broad blade of the sword held in his " \
        "lowered hand. The rider looks at her. Ciri is unable to move. The dead man’s motionless 6 arms wrapped " \
        "around her waist hold her down. She is locked in place by something heavy and wet with blood, " \
        "something which is lying across her thigh, pinning her to the ground. And she is frozen in fear: a terrible " \
        "fear which turns her entrails inside out, which deafens Ciri to the screams of the wounded horse, " \
        "the roar of the blaze, the cries of dying people and the pounding drums. The only thing which exists, " \
        "which counts, which still has any meaning, is fear. Fear embodied in the figure of a black knight wearing a " \
        "helmet decorated with feathers frozen against the wall of raging, red flames. The rider spurs his horse, " \
        "the wings on his helmet fluttering as the bird of prey takes to flight, launching itself to attack its " \
        "helpless victim, paralysed with fear. The bird – or maybe the knight – screeches terrifyingly, cruelly, " \
        "triumphantly. A black horse, black armour, a black flowing cloak, and behind this – flames. A sea of flames. " \
        "Fear. The bird shrieks. The wings beat, feathers slap against her face. Fear! Help! Why doesn’t anyone help " \
        "me? Alone, weak, helpless – I can’t move, can’t force a sound from my constricted throat. Why does no one " \
        "come to help me? I’m terrified! Eyes blaze through the slit in the huge winged helmet. The black cloak veils " \
        "everything— “Ciri!” She woke, numb and drenched in sweat, with her scream – the scream which had woken her – " \
        "still hanging in the air, still vibrating somewhere within her, beneath her breast-bone and burning against " \
        "her parched throat. Her hands ached, clenched around the blanket; her back ached… “Ciri. Calm down.” The " \
        "night was dark and windy, the crowns of the surrounding pine trees rustling steadily and melodiously, " \
        "their limbs and trunks creaking in the wind. There was no malevolent fire, no screams, only this gentle " \
        "lullaby. Beside her the campfire flickered with light and warmth, its reflected flames glowing from harness " \
        "buckles, gleaming red in the leather-wrapped and iron-banded hilt of a sword leaning against a saddle on the " \
        "ground. There was no other fire and no other iron. The hand against her cheek smelled of leather and ashes. " \
        "Not of blood. “Geralt—” “It was just a dream. A bad dream.” 7 Ciri shuddered violently, curling her arms and " \
        "legs up tight. A dream. Just a dream. The campfire had already died down; the birch logs were red and " \
        "luminous, occasionally crackling, giving off tiny spurts of blue flame which illuminated the white hair and " \
        "sharp profile of the man wrapping a blanket and sheepskin around her. “Geralt, I—” “I’m right here. Sleep, " \
        "Ciri. You have to rest. We’ve still a long way ahead of us.” I can hear music, she thought suddenly. Amidst " \
        "the rustling of the trees… there’s music. Lute music. And voices. The Princess of Cintra… A child of " \
        "destiny… A child of Elder Blood, the blood of elves. Geralt of Rivia, the White Wolf, and his destiny. No, " \
        "no, that’s a legend. A poet’s invention. The princess is dead. She was killed in the town streets while " \
        "trying to escape… Hold on… !Hold… “Geralt?” “What, Ciri?” “What did he do to me? What happened? What did he… " \
        "do to me?” “Who?” “The knight… The black knight with feathers on his helmet… I can’t remember anything. He " \
        "shouted… and looked at me. I can’t remember what happened. Only that I was frightened… I was so frightened…” " \
        "The man leaned over her, the flame of the campfire sparkling in his eyes. They were strange eyes. Very " \
        "strange. Ciri had been frightened of them, she hadn’t liked meeting his gaze. But that had been a long time " \
        "ago. A very long time ago. “I can’t remember anything,” she whispered, searching for his hand, as tough and " \
        "coarse as raw wood. “The black knight—” “It was a dream. Sleep peacefully. It won’t come back.” Ciri had " \
        "heard such reassurances in the past. They had been repeated to her endlessly; many, many times she had been " \
        "offered comforting words when her screams had woken her during the night. But this time it was different. " \
        "Now she believed it. Because it was Geralt of Rivia, the White Wolf, the Witcher, who said it. The man who " \
        "was her destiny. The one for whom she was destined. Geralt the Witcher, who had found her surrounded by war, " \
        "death and despair, who had taken her with him and promised they would never part. She fell asleep holding " \
        "tight to his hand. 8 The bard finished the song. Tilting his head a little he repeated the ballad’s refrain " \
        "on his lute, delicately, softly, a single tone higher than the apprentice accompanying him. No one said a " \
        "word. Nothing but the subsiding music and the whispering leaves and squeaking boughs of the enormous oak " \
        "could be heard. Then, all of a sudden, a goat tethered to one of the carts which circled the ancient tree " \
        "bleated lengthily. At that moment, as if given a signal, one of the men seated in the large semi-circular " \
        "audience stood up. Throwing his cobalt blue cloak with gold braid trim back over his shoulder, " \
        "he gave a stiff, dignified bow. “Thank you, Master Dandilion,” he said, his voice resonant without being " \
        "loud. “Allow me, Radcliffe of Oxenfurt, Master of the Arcana, to express what I am sure is the opinion of " \
        "everyone here present and utter words of gratitude and appreciation for your fine art and skill.” The wizard " \
        "ran his gaze over those assembled – an audience of well over a hundred people – seated on the ground, " \
        "on carts, or standing in a tight semicircle facing the foot of the oak. They nodded and whispered amongst " \
        "themselves. Several people began to applaud while others greeted the singer with upraised hands. Women, " \
        "touched by the music, sniffed and wiped their eyes on whatever came to hand, which differed according to " \
        "their standing, profession and wealth: peasant women used their forearms or the backs of their hands, " \
        "merchants’ wives dabbed their eyes with linen handkerchiefs while elves and noblewomen used kerchiefs of the " \
        "finest tight-woven cotton, and Baron Vilibert’s three daughters, who had, along with the rest of his " \
        "retinue, halted their falcon hunt to attend the famous troubadour’s performance, blew their noses loudly and " \
        "sonorously into elegant mouldgreen cashmere scarves. “It would not be an exaggeration to say,” continued the " \
        "wizard, “that you have moved us deeply, Master Dandilion. You have prompted us to reflection and thought; " \
        "you have stirred our hearts. Allow me to express our gratitude, and our respect.” The troubadour stood and " \
        "took a bow, sweeping the heron feather pinned to his fashionable hat across his knees. His apprentice broke " \
        "off his playing, grinned and bowed too, until Dandilion glared at him sternly and snapped something under " \
        "his breath. The boy lowered his head and returned to softly strumming his lute strings. The assembly stirred " \
        "to life. The merchants travelling in the caravan whispered amongst themselves and then rolled a sizable cask " \
        "of beer out to the foot of the oak tree. Wizard Radcliffe lost himself in quiet conversation 9 with Baron " \
        "Vilibert. Having blown their noses, the baron’s daughters gazed at Dandilion in adoration – which went " \
        "entirely unnoticed by the bard, engrossed as he was in smiling, winking and flashing his teeth at a haughty, " \
        "silent group of roving elves, and at one of them in particular: a dark-haired, large-eyed beauty sporting a " \
        "tiny ermine cap. Dandilion had rivals for her attention – the elf, with her huge eyes and beautiful toque " \
        "hat, had caught his audience’s interest as well, and a number of knights, students and goliards were paying " \
        "court to her with their eyes. The elf clearly enjoyed the attention, picking at the lace cuffs of her " \
        "chemise and fluttering her eyelashes, but the group of elves with her surrounded her on all sides, " \
        "not bothering to hide their antipathy towards her admirers. The glade beneath Bleobheris, the great oak, " \
        "was a place of frequent rallies, a well-known travellers’ resting place and meeting ground for wanderers, " \
        "and was famous for its tolerance and openness. The druids protecting the ancient tree called it the Seat of " \
        "Friendship and willingly welcomed all comers. But even during an event as exceptional as the worldfamous " \
        "troubadour’s just-concluded performance the travellers kept to themselves, remaining in clearly delineated " \
        "groups. Elves stayed with elves. Dwarfish craftsmen gathered with their kin, who were often hired to protect " \
        "the merchant caravans and were armed to the teeth. Their groups tolerated at best the gnome miners and " \
        "halfling farmers who camped beside them. All non-humans were uniformly distant towards humans. The humans " \
        "repaid in kind, but were not seen to mix amongst themselves either. Nobility looked down on the merchants " \
        "and travelling salesmen with open scorn, while soldiers and mercenaries distanced themselves from shepherds " \
        "and their reeking sheepskins. The few wizards and their disciples kept themselves entirely apart from the " \
        "others, and bestowed their arrogance on everyone in equal parts. A tight-knit, dark and silent group of " \
        "peasants lurked in the background. Resembling a forest with their rakes, pitchforks and flails poking above " \
        "their heads, they were ignored by all and sundry. The exception, as ever, was the children. Freed from the " \
        "constraints of silence which had been enforced during the bard’s performance, the children dashed into the " \
        "woods with wild cries, and enthusiastically immersed themselves in a game whose rules were incomprehensible " \
        "to all those who had bidden farewell to the happy years of childhood. Children of elves, dwarves, halflings, " \
        "gnomes, half-elves, quarter-elves and toddlers of mysterious provenance neither knew nor recognised racial " \
        "or social divisions. At least, not yet. 10 “Indeed!” shouted one of the knights present in the glade, " \
        "who was as thin as a beanpole and wearing a red and black tunic emblazoned with three lions passant. “The " \
        "wizard speaks the truth! The ballads were beautiful. Upon my word, honourable Dandilion, if you ever pass " \
        "near Baldhorn, my lord’s castle, stop by without a moment’s hesitation. You will be welcomed like a prince– " \
        "what am I saying? Welcomed like King Vizimir himself! I swear on my sword, I have heard many a minstrel, " \
        "but none even came close to being your equal, master. Accept the respect and tributes those of us born to " \
        "knighthood, and those of us appointed to the position, pay to your skills!” Flawlessly sensing the opportune " \
        "moment, the troubadour winked at his apprentice. The boy set his lute aside and picked up a little casket " \
        "which served as a collection box for the audience’s more measurable expressions of appreciation. He " \
        "hesitated, ran his eyes over the crowd, then replaced the little casket and grabbed a large bucket standing " \
        "nearby. Master Dandilion bestowed an approving smile on the young man for his prudence. “Master!” shouted a " \
        "sizeable woman sitting on a cart, the sides of which were painted with a sign for “Vera Loewenhaupt and " \
        "Sons,” and which was full of wickerwork. Her sons, nowhere to be seen, were no doubt busy wasting away their " \
        "mother’s hard-earned fortune. “Master Dandilion, what is this? Are you going to leave us in suspense? That " \
        "can’t be the end of your ballad? Sing to us of what happened next!” “Songs and ballads” – the musician bowed " \
        "– “never end, dear lady, because poetry is eternal and immortal, it knows no beginning, it knows no end—” " \
        "“But what happened next?” The tradeswoman didn’t give up, generously rattling coins into the bucket " \
        "Dandilion’s apprentice held out to her. “At least tell us about it, even if you have no wish to sing of it. " \
        "Your songs mention no names, but we know the witcher you sing of is no other than the famous Geralt of " \
        "Rivia, and the enchantress for whom he burns with love is the equally famous Yennefer. And the Child " \
        "Surprise, destined for the witcher and sworn to him from birth, is Cirilla, the unfortunate Princess of " \
        "Cintra, the town destroyed by the Invaders. Am I right?” Dandilion smiled, remaining enigmatic and aloof. “I " \
        "sing of universal matters, my dear, generous lady,” he stated. “Of emotions which anyone can experience. Not " \
        "about specific people.” “Oh, come on!” yelled a voice from the crowd. “Everyone knows those songs are about " \
        "Geralt the Witcher!” “Yes, yes!” squealed Baron Vilibert’s daughters in chorus, drying their 11 sodden " \
        "scarves. “Sing on, Master Dandilion! What happened next? Did the witcher and Yennefer the Enchantress find " \
        "each other in the end? And did they love each other? Were they happy? We want to know!” “Enough!” roared the " \
        "dwarf leader with a growl in his throat, shaking his mighty waist-length, red beard. “It’s crap – all these " \
        "princesses, sorceresses, destiny, love and women’s fanciful tales. If you’ll pardon the expression, " \
        "great poet, it’s all lies, just a poetic invention to make the story prettier and more touching. But of the " \
        "deeds of war – the massacre and plunder of Cintra, the battles of Marnadal and Sodden – you did sing that " \
        "mightily, Dandilion! There’s no regrets in parting with silver for such a song, a joy to a warrior’s heart! " \
        "And I, Sheldon Skaggs, declare there’s not an ounce of lies in what you say – and I can tell the lies from " \
        "the truth because I was there at Sodden. I stood against the Nilfgaard invaders with an axe in my hand…” “I, " \
        "Donimir of Troy,” shouted the thin knight with three lions passant blazoned across his tunic, “was at both " \
        "battles of Sodden! But I did not see you there, sir dwarf!” “No doubt because you were looking after the " \
        "supply train!” Sheldon Skaggs retorted. “While I was in the front line where things got hot!” “Mind your " \
        "tongue, beardy!” said Donimir of Troy flushing, hitching up his sword belt. “And who you’re speaking to!” " \
        "“Have a care yourself!” The dwarf whacked his palm against the axe wedged in his belt, turned to his " \
        "companions and grinned. “Did you see him there? Frigging knight! See his coat of arms? Ha! Three lions on a " \
        "shield? Two shitting and the third snarling!” “Peace, peace!” A grey-haired druid in a white cloak averted " \
        "trouble with a sharp, authoritative voice. “This is not fitting, gentlemen! Not here, under Bleobheris’ " \
        "crown, an oak older than all the disputes and quarrels of the world! And not in Poet Dandilion’s presence, " \
        "from whose ballads we ought to learn of love, not contention.” “Quite so!” a short, fat priest with a face " \
        "glistening with sweat seconded the druid. “You look but have no eyes, you listen but have deaf ears. Because " \
        "divine love is not in you, you are like empty barrels—” “Speaking of barrels,” squeaked a long-nosed gnome " \
        "from his cart, painted with a sign for “Iron hardware, manufacture and sale”, “roll another out, guildsmen! " \
        "Poet Dandilion’s throat is surely dry – and ours too, from all these emotions!” “—Verily, like empty " \
        "barrels, I tell ye!” The priest, determined not to be put off, drowned out the ironware gnome. “You have " \
        "understood nothing of 12 Master Dandilion’s ballad, you have learned nothing! You did not see that these " \
        "ballads speak of man’s fate, that we are no more than toys in the hands of the gods, our lands no more than " \
        "their playground. The ballads about destiny portrayed the destinies of us all, and the legend of Geralt the " \
        "Witcher and Princess Cirilla – although it is set against the true background of that war – is, after all, " \
        "a mere metaphor, the creation of a poet’s imagination designed to help us—” “You’re talking rubbish, " \
        "holy man!” hollered Vera Loewenhaupt from the heights of her cart. “What legend? What imaginative creation? " \
        "You may not know him, but I know Geralt of Rivia. I saw him with my own eyes in Wyzima, when he broke the " \
        "spell on King Foltest’s daughter. And I met him again later on the Merchants’ Trail, where, at Gildia’s " \
        "request, he slew a ferocious griffin which was preying on the caravans and thus saved the lives of many good " \
        "people. No. This is no legend or fairy-tale. It is the truth, the sincere truth, which Master Dandilion sang " \
        "for us.” “I second that,” said a slender female warrior with her black hair smoothly brushed back and " \
        "plaited into a thick braid. “I, Rayla of Lyria, also know Geralt the White Wolf, the famous slayer of " \
        "monsters. And I’ve met the enchantress, Lady Yennefer, on several occasions – I used to visit Aedirn and her " \
        "home town of Vengerberg. I don’t know anything about their being in love, though.” “But it has to be true," \
        "” the attractive elf in the ermine toque suddenly said in a melodious voice. “Such a beautiful ballad of " \
        "love could not but be true.” “It could not!” Baron Vilibert’s daughters supported the elf and, " \
        "as if on command, wiped their eyes on their scarves. “Not by any measure!” “Honourable wizard!” Vera " \
        "Loewenhaupt turned to Radcliffe. “Were they in love or not? Surely you know what truly happened to them, " \
        "Yennefer and the witcher. Disclose the secret!” “If the song says they were in love,” replied the wizard, " \
        "“then that’s what happened, and their love will endure down the ages. Such is the power of poetry.” “It is " \
        "said,” interrupted Baron Vilibert all of a sudden, “that Yennefer of Vengerberg was killed on Sodden Hill. " \
        "Several enchantresses were killed there—” “That’s not true,” said Donimir of Troy. “Her name is not on the " \
        "monument. I am from those parts and have often climbed Sodden Hill and read the names engraved on the " \
        "monument. Three enchantresses died there: Triss Merigold, Lytta Neyd, known as Coral… hmm… and the name of " \
        "the 13 third has slipped my mind…” The knight glanced at Wizard Radcliffe, who smiled wordlessly. “And this " \
        "witcher,” Sheldon Skaggs suddenly called out, “this Geralt who loved Yennefer, has also bitten the dust, " \
        "apparently. I heard he was killed somewhere in Transriver. He slew and slew monsters until he met his match. " \
        "That’s how it goes: he who fights with the sword dies by the sword. Everyone comes across someone who will " \
        "better them eventually, and is made to taste cold hard iron.” “I don’t believe it.” The slender warrior " \
        "contorted her pale lips, spat vehemently on the ground and crossed her chainmail-clad arms with a crunch. “I " \
        "don’t believe there is anyone to best Geralt of Rivia. I have seen this witcher handle a sword. His speed is " \
        "simply inhuman—” “Well said,” threw in Wizard Radcliffe. “Inhuman. Witchers are mutated, " \
        "so their reactions—” “I don’t understand you, magician.” The warrior twisted her lips even more nastily. " \
        "“Your words are too learned. I know one thing: no swordsman I have ever seen can match Geralt of Rivia, " \
        "the White Wolf. And so I will not accept that he was defeated in battle as the dwarf claims.” “Every " \
        "swordsman’s an arse when the enemy’s not sparse,” remarked Sheldon Skaggs sententiously. “As the elves say.” " \
        "“Elves,” stated a tall, fair-haired representative of the Elder Race coldly, from his place beside the elf " \
        "with the beautiful toque, “are not in the habit of using such vulgar language.” “No! No!” squealed Baron " \
        "Vilibert’s daughters from behind their green scarves. “Geralt the Witcher can’t have been killed! The " \
        "witcher found Ciri, the child destined for him, and then the Enchantress Yennefer, and all three lived " \
        "happily ever after! Isn’t that true, Master Dandilion?” “’Twas a ballad, my noble young ladies,” said the " \
        "beer-parched gnome, manufacturer of ironwares, with a yawn. “Why look for truth in a ballad? Truth is one " \
        "thing, poetry another. Let’s take this – what was her name? – Ciri? The famous Child Surprise. Master " \
        "Dandilion trumped that up for sure. I’ve been to Cintra many a time and the king and queen lived in a " \
        "childless home, with no daughter, no son—” “Liar!” shouted a red-haired man in a sealskin jacket, " \
        "a checked kerchief bound around his forehead. “Queen Calanthe, the Lioness of Cintra, had a daughter called " \
        "Pavetta. She died, together with her husband, in a tempest which struck out at sea, and the depths swallowed " \
        "them both.” “So you see for yourselves I’m not making this up!” The ironware gnome 14 called everyone to be " \
        "his witnesses. “The Princess of Cintra was called Pavetta, not Ciri.” “Cirilla, known as Ciri, " \
        "was the daughter of this drowned Pavetta,” explained the red-haired man. “Calanthe’s granddaughter. She was " \
        "not the princess herself, but the daughter of the Princess of Cintra. She was the Child Surprise destined " \
        "for the witcher, the man to whom – even before she was born – the queen had sworn to hand her granddaughter " \
        "over, just as Master Dandilion has sung. But the witcher could neither find her nor collect her. And here " \
        "our poet has missed the truth.” “Oh yes, he’s missed the truth indeed,” butted in a sinewy young man who, " \
        "judging by his clothes, was a journeyman on his travels prior to crafting his masterpiece and passing his " \
        "master’s exams. “The witcher’s destiny bypassed him: Cirilla was killed during the siege of Cintra. Before " \
        "throwing herself from the tower, Queen Calanthe killed the princess’s daughter with her own hand, " \
        "to prevent her from falling into the Nilfgaardians’ claws alive.” “It wasn’t like that. Not like that at " \
        "all!” objected the red-haired man. “The princess’s daughter was killed during the massacre while trying to " \
        "escape from the town.” “One way or another,” shouted Ironware, “the witcher didn’t find Cirilla! The poet " \
        "lied!” “But lied beautifully,” said the elf in the toque, snuggling up to the tall, fair-haired elf. “It’s " \
        "not a question of poetry but of facts!” shouted the journeyman. “I tell you, the princess’s daughter died by " \
        "her grandmother’s hand. Anyone who’s been to Cintra can confirm that!” “And I say she was killed in the " \
        "streets trying to escape,” declared the redhaired man. “I know because although I’m not from Cintra I served " \
        "in the Earl of Skellige’s troop supporting Cintra during the war. As everyone knows, Eist Tuirseach, " \
        "the King of Cintra, comes from the Skellige Isles. He was the earl’s uncle. I fought in the earl’s troop at " \
        "Marnadal and Cintra and later, after the defeat, at Sodden—” “Yet another veteran,” Sheldon Skaggs snarled " \
        "to the dwarves crowded around him. “All heroes and warriors. Hey, folks! Is there at least one of you out " \
        "there who didn’t fight at Marnadal or Sodden?” “That dig is out of place, Skaggs,” the tall elf reproached " \
        "him, putting his arm around the beauty wearing the toque in a way intended to dispel any lingering doubts " \
        "amongst her admirers. “Don’t imagine you were the only one to fight at Sodden. I took part in the battle as " \
        "well.” 15 “On whose side, I wonder,” Baron Vilibert said to Radcliffe in a highly audible whisper which the " \
        "elf ignored entirely. “As everyone knows,” he continued, sparing neither the baron nor the wizard so much as " \
        "a glance, “over a hundred thousand warriors stood on the field during the second battle of Sodden Hill, " \
        "and of those at least thirty thousand were maimed or killed. Master Dandilion should be thanked for " \
        "immortalising this famous, terrible battle in one of his ballads. In both the lyrics and melody of his work " \
        "I heard not an exaltation but a warning. So I repeat: offer praise and everlasting renown to this poet for " \
        "his ballad, which may, perhaps, prevent a tragedy as horrific as this cruel and unnecessary war from " \
        "occurring in the future.” “Indeed,” said Baron Vilibert, looking defiantly at the elf. “You have read some " \
        "very interesting things into this ballad, honoured sir. An unnecessary war, you say? You’d like to avoid " \
        "such a tragedy in the future, would you? Are we to understand that if the Nilfgaardians were to attack us " \
        "again you would advise that we capitulate? Humbly accept the Nilfgaardian yoke?” “Life is a priceless gift " \
        "and should be protected,” the elf replied coldly. “Nothing justifies wide-scale slaughter and sacrifice of " \
        "life, which is what the battles at Sodden were – both the battle lost and the battle won. Both of them cost " \
        "the humans thousands of lives. And with them, you lost unimaginable potential—” “Elven prattle!” snarled " \
        "Sheldon Skaggs. “Dim-witted rubbish! It was the price that had to be paid to allow others to live decently, " \
        "in peace, instead of being chained, blinded, whipped and forced to work in salt and sulphur mines. Those who " \
        "died a heroic death, those who will now, thanks to Dandilion, live on forever in our memories, taught us to " \
        "defend our own homes. Sing your ballads, Dandilion, sing them to everyone. Your lesson won’t go to waste, " \
        "and it’ll come in handy, you’ll see! Because, mark my words, Nilfgaard will attack us again. If not today, " \
        "then tomorrow! They’re licking their wounds now, recovering, but the day when we’ll see their black cloaks " \
        "and feathered helmets again is growing ever nearer!” “What do they want from us?” yelled Vera Loewenhaupt. " \
        "“Why are they bent on persecuting us? Why don’t they leave us in peace, leave us to our lives and work? What " \
        "do the Nilfgaardians want?” “They want our blood!” howled Baron Vilibert. “And our land!” someone cried from " \
        "the crowd of peasants. “And our women!” chimed in Sheldon Skaggs, with a ferocious glower. Several people " \
        "started to laugh – as quietly and furtively as they could. 16 Even though the idea that anyone other than " \
        "another dwarf would desire one of the exceptionally unattractive dwarf-women was highly amusing, it was not " \
        "a safe subject for teasing or jests – especially not in the presence of the short, stocky, " \
        "bearded individuals whose axes and short-swords had an ugly habit of leaping from their belts and into their " \
        "hands at incredible speed. And the dwarves, for some unknown reason, were entirely convinced that the rest " \
        "of the world was lecherously lying in wait for their wives and daughters, and were extremely touchy about " \
        "it. “This had to happen at some point,” the grey-haired druid declared suddenly. “This had to happen. We " \
        "forgot that we are not the only ones in this world, that the whole of creation does not revolve around us. " \
        "Like stupid, fat, lazy minnows in a slimy pond we chose not to accept the existence of pike. We allowed our " \
        "world, like the pond, to become slimy, boggy and sluggish. Look around you – there is crime and sin " \
        "everywhere, greed, the pursuit of profit, quarrels and disagreements are rife. Our traditions are " \
        "disappearing, respect for our values is fading. Instead of living according to Nature we have begun to " \
        "destroy it. And what have we got for it? The air is poisoned by the stink of smelting furnaces, the rivers " \
        "and brooks are tainted by slaughter houses and tanneries, forests are being cut down without a thought… Ha – " \
        "just look! – even on the living bark of sacred Bleobheris, there just above the poet’s head, there’s a foul " \
        "phrase carved out with a knife – and it’s misspelled at that – by a stupid, illiterate vandal. Why are you " \
        "surprised? It had to end badly—” “Yes, yes!” the fat priest joined in. “Come to your senses, you sinners, " \
        "while there is still time, because the anger and vengeance of the gods hangs over you! Remember Ithlin’s " \
        "oracle, the prophetic words describing the punishment of the gods reserved for a tribe poisoned by crime! " \
        "‘The Time of Contempt will come, when the tree will lose its leaves, the bud will wither, the fruit will " \
        "rot, the seed turn bitter and the river valleys will run with ice instead of water. The White Chill will " \
        "come, and after it the White Light, and the world will perish beneath blizzards.’ Thus spoke Seeress Ithlin! " \
        "And before this comes to pass there will be visible signs, plagues will ravish the earth – Remember! – the " \
        "Nilfgaard are our punishment from the gods! They are the whip with which the Immortals will lash you " \
        "sinners, so that you may —” “Shut up, you sanctimonious old man!” roared Sheldon Skaggs, stamping his heavy " \
        "boots. “Your superstitious rot makes me sick! My guts are churning —” 17 “Careful, Sheldon.” The tall elf " \
        "cut him short with a smile. “Don’t mock another’s religion. It is not pleasant, polite or… safe.” “I’m not " \
        "mocking anything,” protested the dwarf. “I don’t doubt the existence of the gods, but it annoys me when " \
        "someone drags them into earthly matters and tries to pull the wool over my eyes using the prophecies of some " \
        "crazy elf. The Nilfgaardians are the instrument of the gods? Rubbish! Search back through your memories to " \
        "the past, to the days of Dezmod, Radowid and Sambuk, to the days of Abrad, the Old Oak! You may not remember " \
        "them, because your lives are so very short – you’re like Mayflies – but I remember, and I’ll tell you what " \
        "it was like in these lands just after you climbed from your boats on the Yaruga Estuary and the Pontar Delta " \
        "onto the beach. Three kingdoms sprang from the four ships which beached on those shores; the stronger groups " \
        "absorbed the weaker and so grew, strengthening their positions. They invaded others’ territories, " \
        "conquered them, and their kingdoms expanded, becoming ever larger and more powerful. And now the " \
        "Nilfgaardians are doing the same, because theirs is a strong and united, disciplined and tightly knit " \
        "country. And unless you close ranks in the same way, Nilfgaard will swallow you as a pike does a minnow – " \
        "just as this wise druid said!” “Let them just try!” Donimir of Troy puffed out his lion-emblazoned chest and " \
        "shook his sword in its scabbard. “We beat them hollow on Sodden Hill, and we can do it again!” “You’re very " \
        "cocksure,” snarled Sheldon Skaggs. “You’ve evidently forgotten, sir knight, that before the battle of Sodden " \
        "Hill, the Nilfgaard had advanced across your lands like an iron roller, strewing the land between Marnadal " \
        "and Transriver with the corpses of many a gallant fellow like yourself. And it wasn’t loud-mouthed " \
        "smart-arses like you who stopped the Nilfgaardians, but the united strengths of Temeria, Redania, " \
        "Aedirn and Kaedwen. Concord and unity, that’s what stopped them!” “Not just that,” remarked Radcliffe in a " \
        "cold, resonant voice. “Not just that, Master Skaggs.” The dwarf hawked loudly, blew his nose, shuffled his " \
        "feet then bowed a little to the wizard. “No one is denying the contribution of your fellowship,” he said. " \
        "“Shame on he who does not acknowledge the heroism of the brotherhood of wizards on Sodden Hill. They stood " \
        "their ground bravely, shed blood for the common cause, and contributed most eminently to our victory. " \
        "Dandilion did not forget them in his ballad, and nor shall we. But note that these wizards stood united 18 " \
        "and loyal on the Hill, and accepted the leadership of Vilgefortz of Roggeveen just as we, the warriors of " \
        "the Four Kingdoms, acknowledged the command of Vizimir of Redania. It’s just a pity this solidarity and " \
        "concord only lasted for the duration of the war, because, with peace, here we are divided again. Vizimir and " \
        "Foltest are choking each other with customs taxes and trading laws, Demawend of Aedirn is bickering with " \
        "Henselt over the Northern Marches while the League of Hengfors and the Thyssenids of Kovir don’t give a " \
        "toss. And I hear that looking for the old concord amongst the wizards is useless, too. We are not closely " \
        "knit, we have no discipline and no unity. But Nilfgaard does!” “Nilfgaard is ruled by Emperor Emhyr var " \
        "Emreis, a tyrant and autocrat who enforces obedience with whip, noose and axe!” thundered Baron Vilibert. " \
        "“What are you proposing, sir dwarf? How are we supposed to close ranks? With similar tyranny? And which " \
        "king, which kingdom, in your opinion, should subordinate the others? In whose hands would you like to see " \
        "the sceptre and knout?” “What do I care?” replied Skaggs with a shrug. “That’s a human affair. Whoever you " \
        "chose to be king wouldn’t be a dwarf anyway.” “Or an elf, or even half-elf,” added the tall representative " \
        "of the Elder Race, his arm still wrapped around the toque-wearing beauty. “You even consider quarter-elves " \
        "inferior—” “That’s where it stings,” laughed Vilibert. “You’re blowing the same horn as Nilfgaard because " \
        "Nilfgaard is also shouting about equality, promising you a return to the old order as soon as we’ve been " \
        "conquered and they’ve scythed us off these lands. That’s the sort of unity, the sort of equality you’re " \
        "dreaming of, the sort you’re talking about and trumpeting! Nilfgaard pays you gold to do it! And it’s hardly " \
        "surprising you love each other so much, the Nilfgaardians being an elven race—” “Nonsense,” the elf said " \
        "coldly. “You talk rubbish, sir knight. You’re clearly blinded by racism. The Nilfgaardians are human, " \
        "just like you.” “That’s an outright lie! They’re descended from the Black Seidhe and everyone knows it! " \
        "Elven blood flows through their veins! The blood of elves!” “And what flows through yours?” The elf smiled " \
        "derisively. “We’ve been combining our blood for generations, for centuries, your race and mine, and doing so " \
        "quite successfully – fortunately or unfortunately, I don’t know. You started persecuting mixed relationships " \
        "less than a quarter of a century ago and, incidentally, not very successfully. So show me a human now who " \
        "hasn’t 19 a dash of Seidhe Ichaer, the blood of the Elder Race.” Vilibert visibly turned red. Vera " \
        "Loewenhaupt also flushed. Wizard Radcliffe bowed his head and coughed. And, most interestingly, " \
        "the beautiful elf in the ermine toque blushed too. “We are all children of Mother Earth.” The grey-haired " \
        "druid’s voice resounded in the silence. “We are children of Mother Nature. And though we do not respect our " \
        "mother, though we often worry her and cause her pain, though we break her heart, she loves us. Loves us all. " \
        "Let us remember that, we who are assembled here in this Seat of Friendship. And let us not bicker over which " \
        "of us was here first: Acorn was the first to be thrown up by the waves and from Acorn sprouted the Great " \
        "Bleobheris, the oldest of oaks. Standing beneath its crown, amongst its primordial roots, let us not forget " \
        "our own brotherly roots, the earth from which these roots grow. Let us remember the words of Poet " \
        "Dandilion’s song—” “Exactly!” exclaimed Vera Loewenhaupt. “And where is he?” “He’s fled,” ascertained " \
        "Sheldon Skaggs, gazing at the empty place under the oak. “Taken the money and fled without saying goodbye. " \
        "Very elf-like!” “Dwarf-like!” squealed Ironware. “Human-like,” corrected the tall elf, and the beauty in the " \
        "toque rested her head against his shoulder. “Hey, minstrel,” said Mama Lantieri, striding into the room " \
        "without knocking, the scents of hyacinths, sweat, beer and smoked bacon wafting before her. “You’ve got a " \
        "guest. Enter, noble gentleman.” Dandilion smoothed his hair and sat up in the enormous carved armchair. The " \
        "two girls sitting on his lap quickly jumped up, covering their charms and pulling down their disordered " \
        "clothes. The modesty of harlots, thought the poet, was not at all a bad title for a ballad. He got to his " \
        "feet, fastened his belt and pulled on his doublet, all the while looking at the nobleman standing at the " \
        "threshold. “Indeed,” he remarked, “you know how to find me anywhere, though you rarely pick an opportune " \
        "moment. You’re lucky I’d not yet decided which of these two beauties I prefer. And at your prices, Lantieri, " \
        "I cannot afford them both.” Mama Lantieri smiled in sympathy and clapped her hands. Both girls – a " \
        "fair-skinned, freckled islander and a dark-haired half-elf – swiftly left the room. The man at the door " \
        "removed his cloak and handed it to Mama along with a small but well-filled money-bag. 20 “Forgive me, " \
        "master,” he said, approaching the table and making himself comfortable. “I know this is not a good time to " \
        "disturb you. But you disappeared out from beneath the oak so quickly… I did not catch you on the High Road " \
        "as I had intended and did not immediately come across your tracks in this little town. I’ll not take much of " \
        "your time, believe me—” “They always say that, and it’s always a lie,” the bard interrupted. “Leave us " \
        "alone, Lantieri, and see to it that we’re not disturbed. I’m listening, sir.” The man scrutinised him. He " \
        "had dark, damp, almost tearful eyes, a pointed nose and ugly, narrow lips. “I’ll come to the point without " \
        "wasting your time,” he declared, waiting for the door to close behind Mama. “Your ballads interest me, " \
        "master. To be more specific, certain characters of which you sang interest me. I am concerned with the true " \
        "fate of your ballad’s heroes. If I am not mistaken, the true destinies of real people inspired the beautiful " \
        "work I heard beneath the oak tree? I have in mind… Little Cirilla of Cintra. Queen Calanthe’s " \
        "granddaughter.” Dandilion gazed at the ceiling, drumming his fingers on the table. “Honoured sir," \
        "” he said dryly, “you are interested in strange matters. You ask strange questions. Something tells me you " \
        "are not the person I took you to be.” “And who did you take me to be, if I may ask?” “I’m not sure you may. " \
        "It depends if you are about to convey greetings to me from any mutual friends. You should have done so " \
        "initially, but somehow you have forgotten.” “I did not forget at all.” The man reached into the breast " \
        "pocket of his sepia-coloured velvet tunic and pulled out a money-bag somewhat larger than the one he had " \
        "handed the procuress but just as well-filled, which clinked as it touched the table. “We simply have no " \
        "mutual friends, Dandilion. But might this purse not suffice to mitigate the lack?” “And what do you intend " \
        "to buy with this meagre purse?” The troubadour pouted. “Mama Lantieri’s entire brothel and all the land " \
        "surrounding it?” “Let us say that I intend to support the arts. And an artist. In order to chat with the " \
        "artist about his work.” “You love art so much, do you, dear sir? Is it so vital for you to talk to an artist " \
        "that you press money on him before you’ve even introduced yourself and, in doing so, break the most " \
        "elementary rules of courtesy?” “At the beginning of our conversation” – the stranger’s dark eyes narrowed " \
        "imperceptibly – “my anonymity did not bother you.” 21 “And now it is starting to.” “I am not ashamed of my " \
        "name,” said the man, a faint smile appearing on his narrow lips. “I am called Rience. You do not know me, " \
        "Master Dandilion, and that is no surprise. You are too famous and well known to know all of your admirers. " \
        "Yet everyone who admires your talents feels he knows you, knows you so well that a certain degree of " \
        "familiarity is permissible. This applies to me, too. I know it is a misconception, so please graciously " \
        "forgive me.” “I graciously forgive you.” “Then I can count on you agreeing to answer a few questions—” “No! " \
        "No you cannot,” interrupted the poet, putting on airs. “Now, if you will graciously forgive me, " \
        "I am not willing to discuss the subjects of my work, its inspiration or its characters, fictitious or " \
        "otherwise. To do so would deprive poetry of its poetic veneer and lead to triteness.” “Is that so?” “It " \
        "certainly is. For example, if, having sung the ballad about the miller’s merry wife, I were to announce it’s " \
        "really about Zvirka, Miller Loach’s wife, and I included an announcement that Zvirka can most easily be " \
        "bedded every Thursday because on Thursdays the miller goes to market, it would no longer be poetry. It would " \
        "be either rhyming couplets, or foul slander.” “I understand, I understand,” Rience said quickly. “But " \
        "perhaps that is a bad example. I am not, after all, interested in anyone’s peccadilloes or sins. You will " \
        "not slander anyone by answering my questions. All I need is one small piece of information: what really " \
        "happened to Cirilla, the Queen of Cintra’s granddaughter? Many people claim she was killed during the siege " \
        "of the town; there are even eye-witnesses to support the claim. From your ballad, however, it would appear " \
        "that the child survived. I am truly interested to know if this is your imagination at work, or the truth? " \
        "True or false?” “I’m extremely pleased you’re so interested.” Dandilion smiled broadly. “You may laugh, " \
        "Master whatever-your-name-is, but that was precisely what I intended when I composed the ballad. I wished to " \
        "excite my listeners and arouse their curiosity.” “True or false?” repeated Rience coldly. “If I were to give " \
        "that away I would destroy the impact of my work. Goodbye, my friend. You have used up all the time I can " \
        "spare you. And two of my many inspirations are waiting out there, wondering which of them I will choose.” " \
        "Rience remained silent for a long while, making no move to leave. He 22 stared at the poet with his " \
        "unfriendly, moist eyes, and the poet felt a growing unease. A merry din came from the bawdy-house’s main " \
        "room, punctuated from time to time by high-pitched feminine giggles. Dandilion turned his head away, " \
        "pretending to show derisive haughtiness but, in fact, he was judging the distance to the corner of the room " \
        "and the tapestry showing a nymph sprinkling her breasts with water poured from a jug. “Dandilion," \
        "” Rience finally spoke, slipping his hand back into the pocket of his sepia-coloured tunic, “answer my " \
        "questions. Please. I have to know the answer. It’s incredibly important to me. To you, too, believe me, " \
        "because if you answer of your own free will then—” “Then what?” A hide-ous grimace crept over Rience’s " \
        "narrow lips. “Then I won’t have to force you to speak.” “Now listen, you scoundrel.” Dandilion stood up and " \
        "pretended to pull a threatening face. “I loathe violence and force, but I’m going to call Mama Lantieri in a " \
        "minute and she will call a certain Gruzila who fulfils the honourable and responsible role of bouncer in " \
        "this establishment. He is a true artist in his field. He’ll kick your arse so hard you’ll soar over the town " \
        "roofs with such magnificence that the few people passing by at this hour will take you for a Pegasus.” " \
        "Rience made an abrupt gesture and something glistened in his hand. “Are you sure,” he asked, “you’ll have " \
        "time to call her?” Dandilion had no intention of checking if he would have time. Nor did he intend to wait. " \
        "Before the stiletto had locked in Rience’s hand Dandilion had taken a long leap to the corner of the room, " \
        "dived under the nymph tapestry, kicked open a secret door and rushed headlong down the winding stairs, " \
        "nimbly steering himself with the aid of the well-worn banisters. Rience darted after him, but the poet was " \
        "sure of himself – he knew the secret passage like the back of his hand, having used it numerous times to " \
        "flee creditors, jealous husbands and furious rivals from whom he had, from time to time, stolen rhymes and " \
        "tunes. He knew that after the third turning he would be able to grope for a revolving door, behind which " \
        "there was a ladder leading down to the cellar. He was sure that his persecutor would be unable to stop in " \
        "time, would run on and step on a trapdoor through which he would fall and land in the pigsty. He was equally " \
        "sure that – bruised, covered in shit and mauled by the pigs – his persecutor would give up the chase. " \
        "Dandilion was mistaken, as was usually the case whenever he was too confident. Something flashed a sudden " \
        "blue behind his back and the poet felt 23 his limbs grow numb, lifeless and stiff. He couldn’t slow down for " \
        "the revolving door, his legs wouldn’t obey him. He yelled and rolled down the stairs, bumping against the " \
        "walls of the little corridor. The trapdoor opened beneath him with a dry crack and the troubadour tumbled " \
        "down into the darkness and stench. Before thumping his head on the dirt floor and losing consciousness, " \
        "he remembered Mama Lantieri saying something about the pigsty being repaired. The pain in his constricted " \
        "wrists and shoulders, cruelly twisted in their joints, brought him back to his senses. He wanted to scream " \
        "but couldn’t; it felt as though his mouth had been stuck up with clay. He was kneeling on the dirt floor " \
        "with a creaking rope hauling him up by his wrists. He tried to stand, wanting to ease the pressure on his " \
        "shoulders, but his legs, too, were tied together. Choking and suffocating he somehow struggled to his feet, " \
        "helped considerably by the rope which tugged mercilessly at him. Rience was standing in front of him and his " \
        "evil eyes glinted in the light of a lantern held aloft by an unshaven ruffian who stood over six feet tall. " \
        "Another ruffian, probably no shorter, stood behind him. Dandilion could hear his breathing and caught a " \
        "whiff of stale sweat. It was the reeking man who tugged on the rope looped over a roof beam and fastened to " \
        "the poet’s wrists. Dandilion’s feet tore off the dirt floor. The poet whistled through his nose, " \
        "unable to do anything more. “Enough,” Rience snapped at last – he spoke almost immediately, yet it had " \
        "seemed an age to Dandilion. The bard’s feet touched the ground but, despite his most heart-felt desire, " \
        "he could not kneel again – the tight drawn rope was still holding him as taut as a string. Rience came " \
        "closer. There was not even a trace of emotion on his face; the damp eyes had not changed their expression in " \
        "the least. His tone of voice, too, remained calm, quiet, even a little bored. “You nasty rhymester. You " \
        "runt. You scum. You arrogant nobody. You tried to run from me? No one has escaped me yet. We haven’t " \
        "finished our conversation, you clown, you sheep’s head. I asked you a question under much pleasanter " \
        "circumstances than these. Now you are going to answer all my questions, and in far less pleasant " \
        "circumstances. Am I right?” Dandilion nodded eagerly. Only now did Rience smile and make a sign. The bard " \
        "squealed helplessly, feeling the rope tighten and his arms, twisted backwards, cracking in their joints. " \
        "“You can’t talk,” Rience confirmed, still smiling loathsomely, “and it 24 hurts, doesn’t it? For the moment, " \
        "you should know I’m having you strung up like this for my own pleasure – just because I love watching people " \
        "suffer. Go on, just a little higher.” Dandilion was wheezing so hard he almost choked. “Enough," \
        "” Rience finally ordered, then approached the poet and grabbed him by his shirt ruffles. “Listen to me, " \
        "you little cock. I’m going to lift the spell so you can talk. But if you try to raise your charming voice " \
        "any louder than necessary, you’ll be sorry.” He made a gesture with his hand, touched the poet’s cheek with " \
        "his ring and Dandilion felt sensation return to his jaw, tongue and palate. “Now,” Rience continued quietly, " \
        "“I am going to ask you a few questions and you are going to answer them quickly, fluently and " \
        "comprehensively. And if you stammer or hesitate even for a moment, if you give me the slightest reason to " \
        "doubt the truth of your words, then… Look down.” Dandilion obeyed. He discovered to his horror that a short " \
        "rope had been tied to the knots around his ankles, with a bucket full of lime attached to the other end. “If " \
        "I have you pulled any higher,” Rience smiled cruelly, “and this bucket lifts with you, then you will " \
        "probably never regain the feeling in your hands. After that, I doubt you will be capable of playing anything " \
        "on a lute. I really doubt it. So I think you’ll talk to me. Am I right?” Dandilion didn’t agree because he " \
        "couldn’t move his head or find his voice out of sheer fright. But Rience did not seem to require " \
        "confirmation. “It is to be understood,” he stated, “that I will know immediately if you are telling the " \
        "truth, if you try to trick me I will realise straight away, and I won’t be fooled by any poetic ploys or " \
        "vague erudition. This is a trifle for me – just as paralysing you on the stairs was a trifle. So I advise " \
        "you to weigh each word with care, you piece of scum. So, let’s get on with it and stop wasting time. As you " \
        "know, I’m interested in the heroine of one of your beautiful ballads, Queen Calanthe of Cintra’s " \
        "granddaughter, Princess Cirilla, endearingly known as Ciri. According to eye-witnesses this little person " \
        "died during the siege of the town, two years ago. Whereas in your ballad you so vividly and touchingly " \
        "described her meeting a strange, almost legendary individual, the… witcher… Geralt, or Gerald. Leaving the " \
        "poetic drivel about destiny and the decrees of fate aside, from the rest of the ballad it seems the child " \
        "survived the Battle of Cintra in one piece. Is that true?” “I don’t know…” moaned Dandilion. “By all the " \
        "gods, I’m only a poet! I’ve heard this and that, and the rest…” 25 “Well?” “The rest I invented. Made it up! " \
        "I don’t know anything!” The bard howled on seeing Rience give a sign to the reeking man and feeling the rope " \
        "tighten. “I’m not lying!” “True.” Rience nodded. “You’re not lying outright, I would have sensed it. But you " \
        "are beating about the bush. You wouldn’t have thought the ballad up just like that, not without reason. And " \
        "you do know the witcher, after all. You have often been seen in his company. So talk, Dandilion, " \
        "if you treasure your joints. Everything you know.” “This Ciri,” panted the poet, “was destined for the " \
        "witcher. She’s a socalled Child Surprise… You must have heard it, the story’s well known. Her parents swore " \
        "to hand her over to the witcher—” “Her parents are supposed to have handed the child over to that crazed " \
        "mutant? That murderous mercenary? You’re lying, rhymester. Keep such tales for women.” “That’s what " \
        "happened, I swear on my mother’s soul,” sobbed Dandilion. “I have it from a reliable source… The witcher—” " \
        "“Talk about the girl. For the moment I’m not interested in the witcher.” “I don’t know anything about the " \
        "girl! I only know that the witcher was going to fetch her from Cintra when the war broke out. I met him at " \
        "the time. He heard about the massacre, about Calanthe’s death, from me… He asked me about the child, " \
        "the queen’s granddaughter… But I knew everyone in Cintra was killed, not a single soul in the last bastion " \
        "survived—” “Go on. Fewer metaphors, more hard facts!” “When the witcher learned of the massacre and fall of " \
        "Cintra he forsook his journey. We both escaped north. We parted ways in Hengfors and I haven’t seen him " \
        "since… But because he talked, on the way, a bit about this… Ciri, or whatever-her-name-is… and about " \
        "destiny… Well, I made up this ballad. I don’t know any more, I swear!” Rience scowled at him. “And where is " \
        "this witcher now?” he asked. “This hired monster murderer, this poetic butcher who likes to discuss " \
        "destiny?” “I told you, the last time I saw him—” “I know what you said,” Rience interrupted. “I listened " \
        "carefully to what you said. And now you’re going to listen carefully to me. Answer my questions precisely. " \
        "The question is: if no one has seen Geralt, or Gerald, the Witcher for over a year, where is he hiding? " \
        "Where does he usually hide?” “I don’t know where it is,” the troubadour said quickly. “I’m not lying. I 26 " \
        "really don’t know—” “Too quick, Dandilion, too quick.” Rience smiled ominously. “Too eager. You are cunning " \
        "but not careful enough. You don’t know where it is, you say. But I warrant you know what it is.” Dandilion " \
        "clenched his teeth with anger and despair. “Well?” Rience made a sign to the reeking man. “Where is the " \
        "witcher hiding? What is the place called?” The poet remained silent. The rope tightened, twisting his hands " \
        "painfully, and his feet left the ground. Dandilion let out a howl, brief and broken because Rience’s " \
        "wizardly ring immediately gagged him. “Higher, higher.” Rience rested his hands on his hips. “You know, " \
        "Dandilion, I could use magic to sound out your mind, but it’s exhausting. Besides, I like seeing people’s " \
        "eyes pop out of their sockets from pain. And you’re going to tell me anyway.” Dandilion knew he would. The " \
        "rope secured to his ankles grew taut, the bucket of lime scraped along the ground. “Sir,” said the first " \
        "ruffian suddenly, covering the lantern with his cloak and peering through the gap in the pigsty door, " \
        "“someone’s coming. A lass, I think.” “You know what to do,” Rience hissed. “Put the lantern out.” The " \
        "reeking man released the rope and Dandilion tumbled inertly to the ground, falling in such a way that he " \
        "could see the man with the lantern standing at the door and the reeking man, a long knife in his hand, " \
        "lying in wait on the other side. Light broke in from the bawdy-house through gaps in the planks, " \
        "and the poet heard the singing and hubbub. The door to the pigsty creaked open revealing a short figure " \
        "wrapped in a cloak and wearing a round, tightly fitting cap. After a moment’s hesitation, the woman crossed " \
        "the threshold. The reeking man threw himself at her, slashing forcefully with his knife, and tumbled to his " \
        "knees as the knife met with no resistance, passing through the figure’s throat as though through a cloud of " \
        "smoke. Because the figure really was a cloud of smoke – one which was already starting to disperse. But " \
        "before it completely vanished another figure burst into the pigsty, indistinct, dark and nimble as a weasel. " \
        "Dandilion saw it throw a cloak at the lantern man, jump over the reeking one, saw something glisten in its " \
        "hand, and heard the reeking man wheeze and choke savagely. The lantern man disentangled himself from the " \
        "cloak, jumped, took a swing with his knife. A fiery lightning bolt shot from the dark figure with a hiss, " \
        "slapped over the tough’s face and chest with a crack and spread over him 27 like flaming oil. The ruffian " \
        "screamed piercingly and the grim reek of burning meat filled the pigsty. Then Rience attacked. The spell he " \
        "cast illuminated the darkness with a bluish flash in which Dandilion saw a slender woman wearing man’s " \
        "clothes gesticulating strangely with both hands. He only glimpsed her for a second before the blue glow " \
        "disappeared with a bang and a blinding flash. Rience fell back with a roar of fury and collapsed onto the " \
        "wooden pigsty walls, breaking them with a crash. The woman dressed in man’s clothing leapt after him, " \
        "a stiletto flashing in her hand. The pigsty filled with brightness again – this time golden – beaming from a " \
        "bright oval which suddenly appeared in the air. Dandilion saw Rience spring up from the dusty floor, " \
        "leap into the oval and immediately disappear. The oval dimmed but, before it went out entirely, " \
        "the woman ran up to it shouting incomprehensibly, stretching out her hand. Something crackled and rustled " \
        "and the dying oval boiled with roaring flames for a moment. A muffled sound, as if coming from a great " \
        "distance, reached Dandilion’s ears – a sound very much like a scream of pain. The oval went out completely " \
        "and darkness engulfed the pigsty again. The poet felt the power which gagged him disappear. “Help!” he " \
        "howled. “Help!” “Stop yelling, Dandilion,” said the woman, kneeling next to him and slicing through the " \
        "knots with Rience’s stiletto. “Yennefer? Is that you?” “Surely you’re not going to say you don’t remember " \
        "how I look. And I’m sure my voice is not unfamiliar to your musical ear. Can you get up? They didn’t break " \
        "any bones, did they?” Dandilion stood with difficulty, groaned and stretched his aching shoulders. “What’s " \
        "with them?” He indicated the bodies lying on the ground. “We’ll check.” The enchantress snicked the stiletto " \
        "shut. “One of them should still be alive. I’ve a few questions for him.” “This one,” the troubadour stood " \
        "over the reeking man, “probably still lives.” “I doubt it,” said Yennefer indifferently. “I severed his " \
        "windpipe and carotid artery. There might still be a little murmur in him but not for long.” Dandilion " \
        "shuddered. “You slashed his throat?” “If, out of inborn caution, I hadn’t sent an illusion in first, " \
        "I would be the one lying there now. Let’s look at the other one… Bloody hell. Such a sturdy 28 fellow and he " \
        "still couldn’t take it. Pity, pity—” “He’s dead, too?” “He couldn’t take the shock. Hmm… I fried him a " \
        "little too hard… See, even his teeth are charred— What’s the matter with you, Dandilion? Are you going to be " \
        "sick?” “I am,” the poet replied indistinctly, bending over and leaning his forehead against the pigsty wall. " \
        "“That’s everything?” The enchantress put her tumbler down and reached for the skewer of roast chickens. “You " \
        "haven’t lied about anything? Haven’t forgotten anything?” “Nothing. Apart from ‘thank you’. Thank you, " \
        "Yennefer.” She looked him in the eyes and nodded her head lightly, making her glistening, black curls writhe " \
        "and cascade down to her shoulders. She slipped the roast chicken onto a trencher and began dividing it " \
        "skilfully. She used a knife and fork. Dandilion had only known one person, up until then, who could eat a " \
        "chicken with a knife and fork as skilfully. Now he knew how, and from whom, Geralt had learnt the knack. " \
        "Well, he thought, no wonder. After all, he did live with her for a year in Vengerberg and before he left " \
        "her, she had instilled a number of strange things into him. He pulled the other chicken from the skewer and, " \
        "without a second thought, ripped off a thigh and began eating it, pointedly holding it with both hands. “How " \
        "did you know?” he asked. “How did you arrive with help on time?” “I was beneath Bleobheris during your " \
        "performance.” “I didn’t see you.” “I didn’t want to be seen. Then I followed you into town. I waited here, " \
        "in the tavern – it wasn’t fitting, after all, for me to follow you in to that haven of dubious delight and " \
        "certain gonorrhoea. But I eventually became impatient and was wandering around the yard when I thought I " \
        "heard voices coming from the pigsty. I sharpened my hearing and it turned out it wasn’t, as I’d first " \
        "thought, some sodomite but you. Hey, innkeeper! More wine, if you please!” “At your command, honoured lady! " \
        "Quick as a flash!” “The same as before, please, but this time without the water. I can only tolerate water " \
        "in a bath, in wine I find it quite loathsome.” “At your service, at your service!” Yennefer pushed her plate " \
        "aside. There was still enough meat on the chicken, Dandilion noticed, to feed the innkeeper and his family " \
        "for breakfast. A knife and fork were certainly elegant and refined, but they weren’t very 29 effective. " \
        "“Thank you,” he repeated, “for rescuing me. That cursed Rience wouldn’t have spared my life. He’d have " \
        "squeezed everything from me and then butchered me like a sheep.” “Yes, I think he would.” She poured herself " \
        "and the bard some wine then raised her tumbler. “So let’s drink to your rescue and health, Dandilion.” “And " \
        "to yours, Yennefer,” he toasted her in return. “To health for which – as of today – I shall pray whenever " \
        "the occasion arises. I’m indebted to you, beautiful lady, and I shall repay the debt in my songs. I shall " \
        "explode the myth which claims wizards are insensitive to the pain of others, that they are rarely eager to " \
        "help poor, unfortunate, unfamiliar mortals.” “What to do.” She smiled, half-shutting her beautiful violet " \
        "eyes. “The myth has some justification; it did not spring from nowhere. But you’re not a stranger, " \
        "Dandilion. I know you and like you.” “Really?” The poet smiled too. “You have been good at concealing it up " \
        "until now. I’ve even heard the rumour that you can’t stand me, I quote, any more than the plague.” “It was " \
        "the case once.” The enchantress suddenly grew serious. “Later my opinion changed. Later, I was grateful to " \
        "you.” “What for, if I may ask?” “Never mind,” she said, toying with the empty tumbler. “Let us get back to " \
        "more important questions. Those you were asked in the pigsty while your arms were being twisted out of their " \
        "sockets. What really happened, Dandilion? Have you really not seen Geralt since you fled the banks of the " \
        "Yaruga? Did you really not know he returned south after the war? That he was seriously wounded – so " \
        "seriously there were even rumours of his death? Didn’t you know anything?” “No. I didn’t. I stayed in Pont " \
        "Vanis for a long time, in Esterad Thyssen’s court. And then at Niedamir’s in Hengfors—” “You didn’t know.” " \
        "The enchantress nodded and unfastened her tunic. A black velvet ribbon wound around her neck, an obsidian " \
        "star set with diamonds hanging from it. “You didn’t know that when his wounds healed Geralt went to " \
        "Transriver? You can’t guess who he was looking for?” “That I can. But I don’t know if he found her.” “You " \
        "don’t know,” she repeated. “You, who usually know everything, and then sing about everything. Even such " \
        "intimate matters as someone else’s feelings. I listened to your ballads beneath Bleobheris, Dandilion. You " \
        "dedicated a good few verses to me.” 30 “Poetry,” he muttered, staring at the chicken, “has its rights. No " \
        "one should be offended—” “ ‘Hair like a raven’s wing, as a storm in the night…’ ” quoted Yennefer with " \
        "exaggerated emphasis, “ ‘…and in the violet eyes sleep lightning bolts…’ Isn’t that how it went?” “That’s " \
        "how I remembered you.” The poet smiled faintly. “May the first who wishes to claim the description is untrue " \
        "throw the first stone.” “Only I don’t know,” the Enchantress pinched her lips together, “who gave you " \
        "permission to describe my internal organs. How did it go? ‘Her heart, as though a jewel, adorned her neck. " \
        "Hard as if of diamond made, and as a diamond so unfeeling, sharper than obsidian, cutting—’ Did you make " \
        "that up yourself? Or perhaps…?” Her lips quivered, twisted. “…or perhaps you listened to someone’s " \
        "confidences and grievances?” “Hmm…” Dandilion cleared his throat and veered away from the dangerous subject. " \
        "“Tell me, Yennefer, when did you last see Geralt?” “A long time ago.” “After the war?” “After the war…” " \
        "Yennefer’s voice changed a little. “No, I never saw him after the war. For a long time… I didn’t see " \
        "anybody. Well, back to the point, Poet. I am a little surprised to discover that you do not know anything, " \
        "you have not heard anything and that, in spite of this, someone searching for information picked you out to " \
        "stretch over a beam. Doesn’t that worry you?” “It does.” “Listen to me,” she said sharply, banging her " \
        "tumbler against the table. “Listen carefully. Strike that ballad from your repertoire. Do not sing it " \
        "again.” “Are you talking about—” “You know perfectly well what I’m talking about. Sing about the war against " \
        "Nilfgaard. Sing about Geralt and me, you’ll neither harm nor help anyone in the process, you’ll make nothing " \
        "any better or worse. But do not sing about the Lion Cub of Cintra.” She glanced around to check if any of " \
        "the few customers at this hour were eavesdropping, and waited until the lass clearing up had returned to the " \
        "kitchen. “And do try to avoid one-to-one meetings with people you don’t know,” she said quietly. “People who " \
        "‘forget’ to introduce themselves by conveying greetings from a mutual acquaintance. Understand?” 31 He " \
        "looked at her surprised. Yennefer smiled. “Greetings from Dijkstra, Dandilion.” Now the bard glanced around " \
        "timidly. His astonishment must have been evident and his expression amusing because the sorceress allowed " \
        "herself a quite derisive grimace. “While we are on the subject,” she whispered, leaning across the table, " \
        "“Dijkstra is asking for a report. You’re on your way back from Verden and he’s interested in hearing what’s " \
        "being said at King Ervyll’s court. He asked me to convey that this time your report should be to the point, " \
        "detailed and under no circumstances in verse. Prose, Dandilion. Prose.” The poet swallowed and nodded. He " \
        "remained silent, pondering the question. But the enchantress anticipated him. “Difficult times are " \
        "approaching,” she said quietly. “Difficult and dangerous. A time of change is coming. It would be a shame to " \
        "grow old with the uncomfortable conviction that one had done nothing to ensure that these changes are for " \
        "the better. Don’t you agree?” He agreed with a nod and cleared his throat. “Yennefer?” “I’m listening, " \
        "Poet.” “Those men in the pigsty… I would like to know who they were, what they wanted, who sent them. You " \
        "killed them both, but rumour has it that you can draw information even from the dead.” “And doesn’t rumour " \
        "also have it that necromancy is forbidden, by edict of the Chapter? Let it go, Dandilion. Those thugs " \
        "probably didn’t know much anyway. The one who escaped… Hmm… He’s another matter.” “Rience. He was a wizard, " \
        "wasn’t he?” “Yes. But not a very proficient one.” “Yet he managed to escape from you. I saw how he did it – " \
        "he teleported, didn’t he? Doesn’t that prove anything?” “Indeed it does. That someone helped him. Rience had " \
        "neither the time nor the strength to open an oval portal suspended in the air. A portal like that is no " \
        "joke. It’s clear that someone else opened it. Someone far more powerful. That’s why I was afraid to chase " \
        "him, not knowing where I would land. But I sent some pretty hot stuff after him. He’s going to need a lot of " \
        "spells and some effective burn elixirs, and will remain marked for some time.” “Maybe you will be interested " \
        "to hear that he was a Nilfgaardian.” “You think so?” Yennefer sat up and with a swift movement pulled the " \
        "stiletto from her pocket and turned it in her palm. “A lot of people carry Nilfgaardian knives now. They’re " \
        "comfortable and handy – they can even be 32 hidden in a cleavage—” “It’s not the knife. When he was " \
        "questioning me he used the term ‘battle for Cintra’, ‘conquest of the town’ or something along those lines. " \
        "I’ve never heard anyone describe those events like that. For us, it has always been a massacre. The Massacre " \
        "of Cintra. No one refers to it by any other name.” The magician raised her hand, scrutinised her nails. " \
        "“Clever, Dandilion. You have a sensitive ear.” “It’s a professional hazard.” “I wonder which profession you " \
        "have in mind?” She smiled coquettishly. “But thank you for the information. It was valuable.” “Let it be," \
        "” he replied with a smile, “my contribution to making changes for the better. Tell me, Yennefer, " \
        "why is Nilfgaard so interested in Geralt and the girl from Cintra?” “Don’t stick your nose into that " \
        "business.” She suddenly turned serious. “I said you were to forget you ever heard of Calanthe’s " \
        "granddaughter.” “Indeed, you did. But I’m not searching for a subject for a ballad.” “What the hell are you " \
        "searching for then? Trouble?” “Let’s take it,” he said quietly, resting his chin on his clasped hands and " \
        "looking the enchantress in the eye. “Let’s take it that Geralt did, in fact, find and rescue the child. " \
        "Let’s take it that he finally came to believe in the power of destiny, and took the child with him. Where " \
        "to? Rience tried to force it out of me with torture. But you know, Yennefer. You know where the witcher is " \
        "hiding.” “I do.” “And you know how to get there.” “I know that too.” “Don’t you think he should be warned? " \
        "Warned that the likes of Rience are looking for him and the little girl? I would go, but I honestly don’t " \
        "know where it is… That place whose name I prefer not to say…” “Get to the point, Dandilion.” “If you know " \
        "where Geralt is, you ought to go and warn him. You owe him that, Yennefer. There was, after all, " \
        "something between you.” “Yes,” she acknowledged coldly. “There was something between us. That’s why I know " \
        "him a bit. He does not like having help imposed on him. And if he was in need of it he would seek it from " \
        "those he could trust. A year has gone by since those events and I… I’ve not had any news from him. And as " \
        "for our debt, I owe him exactly as much as he owes me. No more and no less.” 33 “So I’ll go then.” He raised " \
        "his head high. “Tell me—” “I won’t,” she interrupted. “Your cover’s blown, Dandilion. They might come after " \
        "you again; the less you know the better. Vanish from here. Go to Redania, to Dijkstra and Philippa Eilhart, " \
        "stick to Vizimir’s court. And I warn you once more: forget the Lion Cub of Cintra. Forget about Ciri. " \
        "Pretend you have never heard the name. Do as I ask. I wouldn’t like anything bad to happen to you. I like " \
        "you too much, owe you too much—” “You’ve said that already. What do you owe me, Yennefer?” The sorceress " \
        "turned her head away, did not say anything for a while. “You travelled with him,” she said finally. “Thanks " \
        "to you he was not alone. You were a friend to him. You were with him.” The bard lowered his eyes. “He didn’t " \
        "get much from it,” he muttered. “He didn’t get much from our friendship. He had little but trouble because " \
        "of me. He constantly had to get me out of some scrape… help me…” She leaned across the table, put her hand " \
        "on his and squeezed it hard without saying anything. Her eyes held regret. “Go to Redania,” she repeated " \
        "after a moment. “To Tretogor. Stay in Dijkstra’s and Philippa’s care. Don’t play at being a hero. You have " \
        "got yourself mixed up in a dangerous affair, Dandilion.” “I’ve noticed.” He grimaced and rubbed his aching " \
        "shoulder. “And that is precisely why I believe Geralt should be warned. You are the only one who knows where " \
        "to look for him. You know the way. I guess you used to be… a guest there…?” Yennefer turned away. Dandilion " \
        "saw her lips pinch, the muscles in her cheek quiver. “Yes, in the past,” she said and there was something " \
        "elusive and strange in her voice. “I used to be a guest there, sometimes. But never uninvited.” The wind " \
        "howled savagely, rippling through the grasses growing over the ruins, rustling in the hawthorn bushes and " \
        "tall nettles. Clouds sped across the sphere of the moon, momentarily illuminating the great castle, " \
        "drenching the moat and few remaining walls in a pale glow undulating with shadows, and revealing mounds of " \
        "skulls baring their broken teeth and staring into nothingness through the black holes of their eye-sockets. " \
        "Ciri squealed sharply and hid her face in the witcher’s cloak. The mare, prodded on by the witcher’s heels, " \
        "carefully stepped over a pile of bricks and passed through the broken arcade. Her horseshoes, ringing 34 " \
        "against the flagstones, awoke weird echoes between the walls, muffled by the howling gale. Ciri trembled, " \
        "digging her hands into the horse’s mane. “I’m frightened,” she whispered. “There’s nothing to be frightened " \
        "of,” replied the witcher, laying his hand on her shoulder. “It’s hard to find a safer place in the whole " \
        "world. This is Kaer Morhen, the Witchers’ Keep. There used to be a beautiful castle here. A long time ago.” " \
        "She did not reply, bowing her head low. The witcher’s mare, called Roach, snorted quietly, as if she too " \
        "wanted to reassure the girl. They immersed themselves in a dark abyss, in a long, unending black tunnel " \
        "dotted with columns and arcades. Roach stepped confidently and willingly, ignoring the impenetrable " \
        "darkness, and her horseshoes rang brightly against the floor. In front of them, at the end of the tunnel, " \
        "a straight, vertical line suddenly flared with a red light. Growing taller and wider it became a door beyond " \
        "which was a faint glow, the flickering brightness of torches stuck in iron mounts on the walls. A black " \
        "figure stood framed in the door, blurred by the brightness. “Who comes?” Ciri heard a menacing, " \
        "metallic voice which sounded like a dog’s bark. “Geralt?” “Yes, Eskel. It’s me.” “Come in.” The witcher " \
        "dismounted, took Ciri from the saddle, stood her on the ground and pressed a bundle into her little hands " \
        "which she grabbed tightly, only regretting that it was too small for her to hide behind completely. “Wait " \
        "here with Eskel,” he said. “I’ll take Roach to the stables.” “Come into the light, laddie,” growled the man " \
        "called Eskel. “Don’t lurk in the dark.” Ciri looked up into his face and barely restrained her frightened " \
        "scream. He wasn’t human. Although he stood on two legs, although he smelled of sweat and smoke, although he " \
        "wore ordinary human clothes, he was not human. No human can have a face like that, she thought. “Well, " \
        "what are you waiting for?” repeated Eskel. She didn’t move. In the darkness she heard the clatter of Roach’s "

tokenized_to_sentences = sent_tokenize(text)
#print(tokenized_to_sentences)
tokenized_to_words = word_tokenize(text)
#print(tokenized_to_words)

# filtering

#nltk.download("stopwords")
from nltk.corpus import stopwords

print(stopwords.words("english"))
stopwords = set(stopwords.words("english"))
filtered = [word for word in tokenized_to_words if word not in stopwords]
#print(filtered)
filtered_again = [word.casefold() for word in tokenized_to_words if word.casefold() not in stopwords and word.isalpha()]
#print(filtered_again)

# Stemming

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
#stemmed = [stemmer.stem(word) for word in filtered_again]
#print(stemmed)

#part of speech

#nltk.download('averaged_perceptron_tagger')
#part_of_speech = nltk.pos_tag(filtered_again)
#print(part_of_speech)

#Lemmatizing

from nltk.stem import WordNetLemmatizer
our_lemmatizer = WordNetLemmatizer()
lemmatized_text = [our_lemmatizer.lemmatize(word) for word in filtered_again]
#print(lemmatized_text)


#dispersion plot
from nltk.draw.dispersion import dispersion_plot
dispersion_plot(filtered_again, ['dandilion', 'poet', 'ciri', 'geralt', 'witcher', 'cintra', 'yennefer'])


from nltk import FreqDist
frequency_distribution = FreqDist(tokenized_to_words)
print(frequency_distribution.most_common(40))
frequency_distribution = FreqDist(filtered_again)
print(frequency_distribution.most_common(20))
frequency_distribution = FreqDist(lemmatized_text)
print(frequency_distribution.most_common(20))

#nltk.download('gutenberg')
hamlet = nltk.corpus.gutenberg.words('carroll-alice.txt')
#print(hamlet[:10])
hamlet_filter = [word.casefold() for word in hamlet if word.casefold() not in stopwords and word.isalpha()]
frequency_distribution = FreqDist(hamlet_filter)
print(frequency_distribution.most_common(40))

#nltk.download('treebank')
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0003.mrg')[0]
t.draw()