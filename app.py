from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

lesson_1_words = {
    "abandon": "desert; leave without planning to come back; quit",
    "keen": "sharp; eager; intense; sensitive",
    "jealous": "afraid that the one you love might prefer someone else; wanting what someone else has",
    "tact": "ability to say the right thing",
    "oath": "a promise that something is true; a curse",
    "vacant": "empty; not filled",
    "hardship": "something that is hard to bear; difficulty",
    "gallant": "brave; showing respect for women",
    "data": "facts; information",
    "unaccustomed": "not used to something",
    "bachelor": "a man who has not married",
    "qualify": "become fit; show that you are able"
}
items1 = list(lesson_1_words.items())
random.shuffle(items1)
lesson_1_words = dict(items1)



lesson_2_words = {
    "corpse": "a dead body, usually of a person",
    "conceal": "hide",
    "dismal": "dark and depressing",
    "frigid": "very cold",
    "inhabit": "live in",
    "numb": "without the power of feeling; deadened",
    "peril": "danger",
    "recline": "lie down; stretch out; lean back",
    "shriek": "scream",
    "sinister": "evil; wicked; dishonest; frightening",
    "tempt": "try to get someone to do something; test; invite",
    "wager": "bet"
}
items2 = list(lesson_2_words.items())
random.shuffle(items2)
lesson_2_words = dict(items2)




lesson_3_words = {
    "typical": "usual; of a kind",
    "minimum": "the least possible amount; the lowest amount",
    "scarce": "hard to get; rare",
    "annual": "once a year; something that appears yearly or lasts for a year",
    "persuade": "win over to do or believe; make willing",
    "essential": "necessary; very important",
    "blend": "mix together thoroughly; a mixture",
    "visible": "able to be seen",
    "expensive": "costly; high-priced",
    "talent": "natural ability",
    "devise": "think out; plan; invent",
    "wholesale": "in large quantity; less than retail in price"
}
items3 = list(lesson_3_words.items())
random.shuffle(items3)
lesson_3_words = dict(items3)

lesson_4_words = {
    "vapor": "moisture in the air that can be seen; fog; mist",
    "eliminate": "get rid of; remove; omit",
    "villain": "a very wicked person",
    "dense": "closely packed together; thick",
    "utilize": "make use of",
    "humid": "moist; damp",
    "theory": "explanation based on thought, observation, or reasoning",
    "descend": "go or come down from a higher place to a lower level",
    "circulate": "go around; go from place to place or person to person",
    "enormous": "extremely large; huge",
    "predict": "tell beforehand",
    "vanish": "disappear; disappear suddenly"
}
items4 = list(lesson_4_words.items())
random.shuffle(items4)
lesson_4_words = dict(items4)

lesson_5_words = {
    "tradition": "beliefs, opinions, and customs handed down from one generation to another",
    "rural": "in the country",
    "burden": "what is carried; a load",
    "campus": "grounds of a college, university, or school",
    "majority": "the larger number; greater part; more than half",
    "assemble": "gather together; bring together",
    "explore": "go over carefully; look into closely; examine",
    "topic": "subject that people think, write, or talk about",
    "debate": "a discussion in which reasons for and against something are brought out",
    "evade": "get away from by trickery or cleverness",
    "probe": "search into; examine thoroughly; investigate",
    "reform": "make better; improve by removing faults"
}
items5 = list(lesson_5_words.items())
random.shuffle(items5)
lesson_5_words = dict(items5)

lesson_6_words = {
    "approach": "come near or nearer to",
    "detect": "find out; discover",
    "defect": "fault; that which is wrong",
    "employee": "a person who works for pay",
    "neglect": "give too little care or attention to",
    "deceive": "make someone believe as true something that is false; mislead",
    "undoubtedly": "certainly; beyond doubt",
    "popular": "liked by most people",
    "thorough": "being all that is needed; complete",
    "client": "person for whom a lawyer acts; customer",
    "comprehensive": "including much; covering completely",
    "defraud": "take money, rights, etc., away by cheating"
}
items6 = list(lesson_6_words.items())
random.shuffle(items6)
lesson_6_words = dict(items6)

lesson_7_words = {
    "postpone": "put off to a later time; delay",
    "consent": "agree; give permission or approval",
    "massive": "big and heavy; large and solid; bulky",
    "capsule": "a small case or covering",
    "preserve": "keep from harm or change; keep safe; protect",
    "denounce": "condemn in public; express strong disapproval of",
    "unique": "having no like or equal; being the only one of its kind",
    "torrent": "any violent, rushing stream; flood",
    "resent": "feel injured and angered at (something)",
    "molest": "interfere with and trouble; disturb",
    "gloomy": "dark; dim; in low spirits",
    "unforeseen": "not known beforehand; unexpected"
}
items7 = list(lesson_7_words.items())
random.shuffle(items7)
lesson_7_words = dict(items7)

lesson_8_words = {
    "exaggerate": "make something greater than it is; overstate",
    "amateur": "person who does something for pleasure, not for money or as a profession",
    "mediocre": "neither good nor bad; average; ordinary",
    "variety": "lack of sameness; a number of different things",
    "valid": "supported by facts or authority; sound; true",
    "survive": "live longer than; remain alive after",
    "weird": "mysterious; unearthly",
    "prominent": "well-known; important",
    "security": "freedom from danger, care, or fear; feeling or condition of being safe",
    "bulky": "taking up much space; large",
    "reluctant": "unwilling",
    "obvious": "easily seen or understood; clear to the eye or mind; not to be doubted; plain"
}
items8 = list(lesson_8_words.items())
random.shuffle(items8)
lesson_8_words = dict(items8)

lesson_9_words = {
    "vicinity": "region near a place; neighborhood",
    "century": "100 years",
    "rage": "violent anger; something that arouses intense but brief enthusiasm",
    "document": "something handwritten or printed that gives information or proof of some fact",
    "conclude": "end; finish; decide",
    "undeniable": "not to be denied; cannot be questioned",
    "resist": "act against; strive against; oppose",
    "lack": "be entirely without something; have not enough",
    "ignore": "pay no attention to; disregard",
    "challenge": "call to a fight",
    "miniature": "represented on a small scale",
    "source": "place from which something comes or is obtained"
}
items9 = list(lesson_9_words.items())
random.shuffle(items9)
lesson_9_words = dict(items9)


lesson_10_words = {
    "excel": "be better than; do better than",
    "feminine": "of women or girls",
    "mount": "get up on",
    "compete": "try hard to get something wanted by others; be a rival",
    "dread": "look forward to with fear; fear greatly; causing great fear",
    "masculine": "of man; male",
    "menace": "threat",
    "tendency": "leaning; movement in a certain direction",
    "underestimate": "set too low a value, amount, or rate",
    "victorious": "having won a victory; conquering",
    "numerous": "very many; several",
    "flexible": "easily bent; willing to yield"
}
items10 = list(lesson_10_words.items())
random.shuffle(items10)
lesson_10_words = dict(items10)

lesson_11_words = {
    "evidence": "that which makes clear the truth or falsehood of something",
    "solitary": "alone; single; only",
    "vision": "power of seeing; sense of sight",
    "frequent": "happening often; occurring repeatedly",
    "glimpse": "a short, quick view",
    "recent": "done, made, or occurring not long ago",
    "decade": "ten years",
    "hesitate": "fail to act quickly; be undecided",
    "absurd": "plainly not true or sensible; foolish",
    "conflict": "direct opposition; disagreement",
    "minority": "smaller number or part; less than half",
    "fiction": "that which is imagined or made up"
}
items11 = list(lesson_11_words.items())
random.shuffle(items11)
lesson_11_words = dict(items11)


lesson_12_words = {
    "ignite": "set on fire",
    "abolish": "do away with completely; put an end to",
    "urban": "of or having to do with cities or towns",
    "population": "people of a city or country",
    "frank": "free in expressing one's real thoughts, opinions, or feelings; not hiding what is in one's mind",
    "pollute": "make dirty",
    "reveal": "make known",
    "prohibit": "forbid by law or authority",
    "urgent": "demanding immediate action or attention; important",
    "adequate": "as much as is needed; fully sufficient",
    "decrease": "make or become less",
    "audible": "able to be heard"
}
items12 = list(lesson_12_words.items())
random.shuffle(items12)
lesson_12_words = dict(items12)

lesson_13_words = {
    "journalist": "one who writes for, edits, manages, or produces a newspaper or magazine",
    "famine": "starvation; great shortage",
    "revive": "bring back or come back to life or consciousness",
    "commence": "begin; start",
    "observant": "quick to notice; watchful",
    "identity": "recognize as being, or show to be, a certain person or thing; prove to be the same",
    "migrate": "move from one place to another",
    "vessel": "a ship; a hollow container; tube containing body fluid",
    "persist": "continue firmly; refuse to stop or be changed",
    "hazy": "misty; smoky; unclear",
    "gleam": "a flash or beam of light",
    "editor": "person who prepares a publication; one who corrects a manuscript and helps to improve it"
}
items13 = list(lesson_13_words.items())
random.shuffle(items13)
lesson_13_words = dict(items13)

lesson_14_words = {
    "unruly": "hard to rule or control; lawless",
    "rival": "person who wants and tries to get the same thing as another; one who tries to equal or do better than another",
    "violent": "acting or done with strong, rough force",
    "brutal": "coarse and savage; like a brute; cruel",
    "opponent": "person who is on the other side of a fight, game, or discussion; person fighting, struggling or speaking against another",
    "brawl": "a noisy quarrel or fight",
    "duplicate": "an exact copy; make an exact copy of; repeat exactly",
    "vicious": "evil; wicked; savage",
    "whirling": "turning or swinging round and round; spinning",
    "underdog": "person having the worst of any struggle; one who is expected to lose",
    "thrust": "push with force",
    "bewildered": "confused completely; puzzled"
}
items14 = list(lesson_14_words.items())
random.shuffle(items14)
lesson_14_words = dict(items14)


lesson_15_words = {
    "expand": "increase in size; enlarge; swell",
    "alter": "make different; change; vary",
    "mature": "ripe; fully grown or developed",
    "sacred": "worthy of respect; holy",
    "revise": "change; alter; bring up to date",
    "pledge": "promise",
    "casual": "happening by chance; not planned or expected; not calling attention to itself",
    "pursue": "follow; proceed along",
    "unanimous": "in complete agreement",
    "fortunate": "having good luck; lucky",
    "pioneer": "one who goes first or prepares a way for others",
    "innovative": "fresh; clever; having new ideas"
}
items15 = list(lesson_15_words.items())
random.shuffle(items15)
lesson_15_words = dict(items15)


lesson_16_words = {
    "slender": "long and thin; limited; slight",
    "surpass": "do better than; be greater than; excel",
    "vast": "very great; enormous",
    "doubt": "not believe; not be sure of; feel uncertain about; lack of certainty",
    "capacity": "amount of room or space inside; largest amount that can be held by a container",
    "penetrate": "get into or through",
    "pierce": "go into; go through; penetrate",
    "accurate": "exactly right as the result of care or pains",
    "microscope": "instrument with a lens for making objects larger so that one can see things more clearly",
    "grateful": "feeling gratitude; thankful",
    "cautious": "very careful; never taking chances",
    "confident": "firmly believing; certain; sure"
}
items16 = list(lesson_16_words.items())
random.shuffle(items16)
lesson_16_words = dict(items16)


lesson_17_words = {
    "slender": "long and thin; limited; slight",
    "surpass": "do better than; be greater than; excel",
    "vast": "very great; enormous",
    "doubt": "not believe; not be sure of; feel uncertain about; lack of certainty",
    "capacity": "amount of room or space inside; largest amount that can be held by a container",
    "penetrate": "get into or through",
    "pierce": "go into; go through; penetrate",
    "accurate": "exactly right as the result of care or pains",
    "microscope": "instrument with a lens for making objects larger so that one can see things more clearly",
    "grateful": "feeling gratitude; thankful",
    "cautious": "very careful; never taking chances",
    "confident": "firmly believing; certain; sure"
}
items17 = list(lesson_17_words.items())
random.shuffle(items17)
lesson_17_words = dict(items17)

lesson_18_words = {
    "appeal": "attraction; interest; to urge",
    "addict": "one who cannot break away from a habit or practice",
    "wary": "on one's guard against danger or trickery; cautious",
    "aware": "knowing; realizing",
    "misfortune": "bad luck",
    "avoid": "keep away from; keep out of the way of",
    "wretched": "very unsatisfactory; miserable",
    "keg": "small barrel, usually holding less than ten gallons",
    "nourish": "make or keep alive and well, with food; feed; develop an attitude",
    "harsh": "rough to the touch, taste, eye, or ear; sharp",
    "quantity": "amount",
    "opt": "choose or favor; select"
}
items18 = list(lesson_18_words.items())
random.shuffle(items18)
lesson_18_words = dict(items18)


lesson_19_words = {
    "harvest": "gathering in of grain or other food crops",
    "abundant": "more than enough; very plentiful",
    "uneasy": "restless; disturbed; anxious",
    "calculate": "find out by adding, subtracting, multiplying, or dividing; figure",
    "absorb": "take in or suck up (liquids); interest greatly",
    "estimate": "form a judgment or opinion about; guess",
    "morsel": "a small bite; mouthful; tiny amount",
    "quota": "share of a total due from or to a particular state, district, person, etc.",
    "threat": "sign or cause of possible evil or harm",
    "ban": "prohibit; forbid",
    "panic": "unreasoning fear; fear spreading through a group of people so that they lose control of themselves",
    "appropriate": "fit; set apart for some special use"
}
items19 = list(lesson_19_words.items())
random.shuffle(items19)
lesson_19_words = dict(items19)

lesson_20_words = {
    "emerge": "come out; come up; come into view",
    "jagged": "with sharp points sticking out; unevenly cut or torn",
    "linger": "stay on; go slowly as if unwilling to leave",
    "ambush": "a trap in which soldiers or other enemies hide to make a surprise attack",
    "crafty": "skillful in deceiving others; sly; tricky",
    "defiant": "openly resisting; challenging",
    "vigor": "active strength or force",
    "perish": "be destroyed; die",
    "fragile": "easily broken, damaged, or destroyed; delicate",
    "captive": "prisoner",
    "prosper": "be successful; have good fortune",
    "devour": "eat hungrily; absorb completely; take in greedily"
}
items20 = list(lesson_20_words.items())
random.shuffle(items20)
lesson_20_words = dict(items20)


lesson_21_words = {
    "plea": "request; appeal; that which is asked of another",
    "weary": "tired",
    "collide": "come together with force",
    "confirm": "prove to be true or correct; make certain",
    "verify": "prove to be true; confirm",
    "anticipate": "look forward to; expect",
    "dilemma": "situation requiring a choice between two evils; a difficult choice",
    "detour": "a roundabout way",
    "merit": "goodness; worth; value",
    "transmit": "send over; pass on; pass along; let through",
    "relieve": "make less; make easier; reduce the pain of; release; free",
    "baffle": "be too hard to understand or solve"
}

# Shuffle the words
items21 = list(lesson_21_words.items())
random.shuffle(items21)
lesson_21_words = dict(items21)



lesson_22_words = {
    "warden": "keeper; guard; person in charge of a prison",
    "acknowledge": "admit to be true",
    "justice": "just conduct; fair dealing",
    "delinquent": "an offender; criminal; behind time",
    "reject": "refuse to take, use, believe, consider, grant, etc.",
    "deprive": "take away from by force",
    "spouse": "husband or wife",
    "vocation": "occupation; business; profession; trade",
    "unstable": "not firmly fixed; easily moved or overthrown",
    "homicide": "a killing of one human being by another; murder",
    "penalize": "declare punishable by law or rule; set a penalty for",
    "beneficiary": "person who receives benefit"
}


# Shuffle the words
items22 = list(lesson_22_words.items())
random.shuffle(items22)
lesson_22_words = dict(items22)






lesson_23_words = {
    "reptile": "a cold-blooded animal that creeps or crawls; snakes, lizards, turtles, alligators, and crocodiles",
    "rarely": "seldom; not often",
    "forbid": "order someone not to do something; make a rule against",
    "logical": "reasonable; reasonably expected",
    "exhibit": "display; show",
    "proceed": "go on after having stopped; move forward",
    "precaution": "measures taken beforehand; foresight",
    "extract": "pull out or draw out, usually with some effort",
    "prior": "coming before; earlier",
    "embrace": "hug one another; a hug",
    "valiant": "brave; courageous",
    "partial": "not complete; not total"
}

# Shuffle the words
items23 = list(lesson_23_words.items())
random.shuffle(items23)
lesson_23_words = dict(items23)



lesson_24_words = {
    "fierce": "savage; wild",
    "detest": "dislike very much; hate",
    "sneer": "show scorn or contempt by looks or words; a scornful look or remark",
    "scowl": "look angry by lowering the eyebrows; frown",
    "encourage": "give courage to; increase the confidence of",
    "consider": "think about in order to decide",
    "vermin": "small animals that are troublesome or destructive; fleas, bedbugs, lice, rats, and mice are vermin",
    "wail": "cry loud and long because of grief or pain",
    "symbol": "something that stands for or represents something else",
    "authority": "the right to command or enforce obedience; power delegated to another; an author or volume that may be appealed to in support of an action or belief",
    "neutral": "on neither side of a quarrel or war",
    "trifle": "a small amount; little bit; something of little value"
}

# Shuffle the words
items24 = list(lesson_24_words.items())
random.shuffle(items24)
lesson_24_words = dict(items24)




lesson_25_words = {
    "architect": "a person who makes plans for buildings and other structures; a maker; a creator",
    "matrimony": "married life; ceremony of marriage",
    "baggage": "the trunks and suitcases a person takes when he or she travels; an army's equipment",
    "squander": "spend foolishly; waste",
    "abroad": "outside one's country; going around; far and wide",
    "fugitive": "a runaway",
    "calamity": "a great misfortune; serious trouble",
    "pauper": "a very poor person",
    "envy": "jealousy; the object of jealousy; to feel jealous",
    "collapse": "a breakdown; to fall in; break down; fail suddenly; fold together",
    "prosecute": "bring before a court; follow up; carry on",
    "bigamy": "having two wives or two husbands at the same time"
}

# Shuffle the words
items25 = list(lesson_25_words.items())
random.shuffle(items25)
lesson_25_words = dict(items25)



lesson_26_words = {
    "possible": "able to be, be done, or happen; able to be true; able to be done or chosen properly",
    "compel": "force; get by force",
    "awkward": "clumsy; not well-suited to use; not easily managed; embarrassing",
    "venture": "a daring undertaking; an attempt to make money by taking business risks; to dare; to expose to risk",
    "awesome": "causing or showing great fear, wonder, or respect",
    "guide": "a person who shows the way; to direct; to manage",
    "quench": "put an end to; drown or put out",
    "betray": "give away to the enemy; be unfaithful; mislead; show",
    "utter": "speak; make known; express",
    "pacify": "make calm; quiet down; bring peace to",
    "respond": "answer; react",
    "beckon": "signal by a motion of the hand or head; attract"
}

# Shuffle the words
items26 = list(lesson_26_words.items())
random.shuffle(items26)
lesson_26_words = dict(items26)



lesson_27_words = {
    "despite": "in spite of",
    "disrupt": "upset; cause to break down",
    "rash": "too hasty or careless; a breaking out with many small red spots on the skin",
    "rapid": "very quick; swift",
    "exhaust": "empty completely; use up; tire out",
    "severity": "strictness; harshness; plainness; violence",
    "feeble": "weak",
    "unite": "join together; become one",
    "cease": "stop",
    "thrifty": "saving; careful in spending; thriving",
    "miserly": "stingy; like a miser",
    "monarch": "king or queen; ruler"
}

# Shuffle the words
items27 = list(lesson_27_words.items())
random.shuffle(items27)
lesson_27_words = dict(items27)


lesson_28_words = {
    "outlaw": "an exile; an outcast; a criminal; to declare unlawful",
    "promote": "raise in rank or importance; help to grow and develop",
    "undernourished": "not sufficiently fed",
    "illustrate": "make clear or explain by stories, examples, comparisons, or other means",
    "disclose": "uncover; make known",
    "excessive": "too much; too great; extreme",
    "disaster": "an event that causes much suffering or loss; a great misfortune",
    "censor": "person who tells others how they ought to behave; one who changes works to make them acceptable to the government",
    "culprit": "offender; person guilty of a fault or crime",
    "juvenile": "young; youthful; of or for boys and girls; a young person",
    "bait": "anything used to attract fish or animals; anything used to tempt or attract a person",
    "insist": "keep firmly to some demand, statement, or position"
}

# Shuffle the words
items28 = list(lesson_28_words.items())
random.shuffle(items28)
lesson_28_words = dict(items28)


lesson_29_words = {
    "toil": "hard work; to work hard; move with difficulty",
    "blunder": "stupid mistake; to make a stupid mistake; stumble; say clumsily",
    "daze": "confuse",
    "mourn": "grieve; feel or show sorrow for",
    "subside": "sink to a lower level; grow less",
    "maim": "cripple; disable; cause to lose an arm, leg, or other part of the body",
    "comprehend": "understand",
    "commend": "praise; hand over for safekeeping",
    "final": "coming last; deciding",
    "exempt": "make free from; freed from",
    "vain": "having too much pride in one's ability, looks, etc.; of no use",
    "repetition": "act of doing or saying again"
}

# Shuffle the words
items29 = list(lesson_29_words.items())
random.shuffle(items29)
lesson_29_words = dict(items29)


lesson_30_words = {
    "depict": "represent by drawing or painting; describe",
    "mortal": "sure to die sometime; deadly; pertaining to or causing death",
    "novel": "new; a long story with characters and plot",
    "occupant": "person in possession of a house, office, or position",
    "appoint": "decide on; set a time or place; choose for a position",
    "quarter": "region; section; a place to live",
    "site": "position or place (of anything)",
    "quote": "repeat exactly the words of another; give the price of",
    "verse": "a short division of a chapter in the Bible; a line of poetry",
    "morality": "the right or wrong of an action; virtue; principles of conduct",
    "roam": "wander; go about with no special plan or aim",
    "attract": "draw to oneself; win the attention and liking of"
}

# Shuffle the words
items30 = list(lesson_30_words.items())
random.shuffle(items30)
lesson_30_words = dict(items30)


lesson_31_words = {
    "commuter": "one who travels regularly, especially over a considerable distance, between home and work",
    "confine": "keep in; hold in",
    "idle": "not doing anything; not busy; lazy; without any good reason or cause; to waste (time)",
    "idol": "a thing, usually an image, that is worshiped; a person or thing that is loved very much",
    "jest": "joke; fun; mockery; thing to be laughed at; to joke; poke fun",
    "patriotic": "loving one's country; showing love and loyal support for one's country",
    "dispute": "disagree; oppose; try to win; a debate or disagreement",
    "valor": "bravery; courage",
    "lunatic": "crazy person; insane; extremely foolish",
    "vein": "mood; a blood vessel that carries blood to the heart; a crack or seam in a rock filled with a different mineral",
    "uneventful": "without important or striking happenings",
    "fertile": "bearing seeds or fruit; producing much of anything"
}

# Shuffle the words if needed
items31 = list(lesson_31_words.items())
random.shuffle(items31)
lesson_31_words = dict(items31)


lesson_32_words = {
    "refer": "hand over; send, direct, or turn for information, help, or action; (refer to) direct attention to or speak about; assign to or think of as caused by",
    "distress": "great pain or sorrow; misfortune; dangerous or difficult situation; to cause pain or make unhappy",
    "diminish": "make or become smaller in size, amount, or importance",
    "maximum": "greatest amount; greatest possible",
    "flee": "run away; go quickly",
    "vulnerable": "capable of being injured; open to attack, sensitive to criticism, influences, etc.",
    "signify": "mean; be a sign of; make known by signs, words, or actions; have importance",
    "mythology": "legends or stories that usually attempt to explain something in nature",
    "provide": "to supply; to state as a condition; to prepare for or against some situation",
    "colleague": "associate; fellow worker",
    "torment": "cause very great pain to; worry or annoy very much; cause of very great pain; very great pain",
    "loyalty": "faithfulness to a person, government, idea, custom, or the like"
}

# Shuffle the words if needed
items32 = list(lesson_32_words.items())
random.shuffle(items32)
lesson_32_words = dict(items32)


lesson_33_words = {
    "volunteer": "person who enters any service of his or her own free will; to offer one's services",
    "prejudice": "an opinion formed without taking time and care to judge fairly; to harm or injure",
    "shrill": "having a high pitch; high and sharp in sound; piercing",
    "jolly": "merry; full of fun",
    "witty": "cleverly amusing",
    "hinder": "hold back; make hard to do",
    "lecture": "speech or planned talk; a scolding; to scold",
    "abuse": "make bad use of; use wrongly; treat badly; scold very severely; bad or wrong use; bad treatment",
    "mumble": "speak indistinctly",
    "mute": "silent; unable to speak",
    "wad": "small, soft mass; to roll or crush into a small mass",
    "retain": "keep; remember; employ by payment of a fee"
}

# Shuffle the words if needed
items33 = list(lesson_33_words.items())
random.shuffle(items33)
lesson_33_words = dict(items33)


lesson_34_words = {
    "candidate": "person who is proposed for some office or honor",
    "precede": "go before; come before; be higher in rank or importance",
    "adolescent": "growing up to manhood or womanhood; youthful; a person from about 13 to 22 years of age",
    "coeducational": "having to do with educating both sexes in the same school",
    "radical": "going to the root; fundamental; extreme; person with extreme opinions",
    "spontaneous": "of one's own free will; natural; on the spur of the moment; without rehearsal",
    "skim": "remove from the top; move lightly (over); glide along; read hastily or carelessly",
    "vaccinate": "inoculate with vaccine as a protection against smallpox and other diseases",
    "untidy": "not neat; not in order",
    "utensil": "container or tool used for practical purposes",
    "sensitive": "receiving impressions readily; easily affected or influenced; easily hurt or offended",
    "temperate": "not very hot and not very cold; moderate"
}

# Shuffle the words if needed
items34 = list(lesson_34_words.items())
random.shuffle(items34)
lesson_34_words = dict(items34)


lesson_35_words = {
    "vague": "not definite; not clear; not distinct",
    "elevate": "raise; lift up",
    "lottery": "a scheme for distributing prizes by lot or chance",
    "finance": "money matters; to provide money for",
    "obtain": "get; be in use",
    "cinema": "moving picture",
    "event": "happening; important happening; result or outcome; one item in a program of sports",
    "discard": "throw aside",
    "soar": "fly upward or at a great height; aspire",
    "subsequent": "later; following; coming after",
    "relate": "tell; give an account of; connect in thought or meaning",
    "stationary": "having a fixed station or place; standing still; not moving; not changing in size, number or activity"
}

# Shuffle the words if needed
items35 = list(lesson_35_words.items())
random.shuffle(items35)
lesson_35_words = dict(items35)



lesson_36_words = {
    "prompt": "quick; on time; done at once; to cause (someone) to do something; remind (someone) of the words or actions needed",
    "hasty": "quick; hurried; not well thought out",
    "scorch": "burn slightly; dry up; criticize sharply",
    "tempest": "violent storm with much wind; a violent disturbance",
    "soothe": "quiet; calm; comfort",
    "sympathetic": "having or showing kind feelings toward others; approving; enjoying the same things and getting along well together",
    "redeem": "buy back; pay off; carry out; set free; make up for",
    "resume": "begin again; go on; take again",
    "harmony": "situation of getting on well together or going well together; sweet or musical sound",
    "refrain": "hold back",
    "illegal": "not lawful; against the law",
    "narcotic": "drug that produces drowsiness, sleep, dullness, or an insensible condition, and lessens pain by dulling the nerves"
}

# Shuffle the words if needed
items36 = list(lesson_36_words.items())
random.shuffle(items36)
lesson_36_words = dict(items36)

lesson_37_words = {
    "heir": "person who has a right to someone's property after that one dies; person who inherits anything",
    "majestic": "grand; noble; dignified; kingly",
    "dwindle": "become smaller and smaller; shrink",
    "surplus": "amount over and above what is needed; excess, extra",
    "traitor": "person who betrays his or her country, a friend, duty, etc.",
    "deliberate": "to consider carefully; intended; done on purpose; slow and careful, as though allowing time to decide what to do",
    "vandal": "person who willfully or ignorantly destroys or damages beautiful things",
    "drought": "long period of dry weather; lack of rain; lack of water; dryness",
    "abide": "accept and follow out; remain faithful to; dwell; endure",
    "unify": "unite; make or form into one",
    "summit": "highest point; top",
    "heed": "give careful attention to; take notice of; careful attention"
}

# Shuffle the words if needed
items37 = list(lesson_37_words.items())
random.shuffle(items37)
lesson_37_words = dict(items37)


lesson_38_words = {
    "biography": "the written story of a person's life; the part of literature that consists of biographies",
    "drench": "wet thoroughly; soak",
    "swarm": "group of insects flying or moving about together; crowd or great number; to fly or move about in great numbers",
    "wobble": "move unsteadily from side to side",
    "tumult": "noise; uproar; violent disturbance or disorder",
    "kneel": "go down on one's knees; remain on the knees",
    "dejected": "in low spirits; sad",
    "obedient": "doing what one is told; willing to obey",
    "recede": "go back; move back; slope backward; withdraw",
    "tyrant": "cruel or unjust ruler; cruel master; absolute ruler",
    "charity": "generous giving to the poor; institutions for helping the sick, the poor, or the helpless; kindness in judging people's faults",
    "verdict": "decision of a jury; judgment"
}

# Shuffle the words if needed
items38 = list(lesson_38_words.items())
random.shuffle(items38)
lesson_38_words = dict(items38)


lesson_39_words = {
    "unearth": "dig up; discover; find out",
    "depart": "go away; leave; turn away (from); change; die",
    "coincide": "occupy the same place in space; occupy the same time; correspond exactly; agree",
    "cancel": "cross out; mark so that it cannot be used; wipe out; call off",
    "debtor": "person who owes something to another",
    "legible": "able to be read; easy to read; plain and clear",
    "placard": "a notice to be posted in a public place; poster",
    "contagious": "spreading by contact, easily spreading from one to another",
    "clergy": "persons prepared for religious work; clergymen as a group",
    "customary": "usual",
    "transparent": "easily seen through; clear",
    "scald": "pour boiling liquid over; burn with hot liquid or steam; heat almost to the boiling point"
}

# Shuffle the words if needed
items39 = list(lesson_39_words.items())
random.shuffle(items39)
lesson_39_words = dict(items39)


lesson_40_words = {
    "epidemic": "an outbreak of a disease that spreads rapidly so that many people have it at the same time; widespread",
    "obesity": "extreme fatness",
    "magnify": "cause to look larger than it really is; make too much of; go beyond the truth in telling",
    "chiropractor": "a person who treats ailments by massage and manipulation of the vertebrae and other forms of therapy on the theory that disease results from interference with the normal functioning of the nervous system",
    "obstacle": "anything that gets in the way or hinders; impediment; obstruction",
    "ventilate": "change the air in; purify by fresh air; discuss openly",
    "jeopardize": "risk; endanger",
    "negative": "saying no; minus; showing the lights and shadows reversed",
    "pension": "regular payment that is not wages; to make such a payment",
    "vital": "having to do with life; necessary to life; causing death, failure or ruin; lively",
    "municipal": "of a city or state; having something to do in the affairs of a city or town",
    "oral": "spoken; using speech; of the mouth"
}

# Shuffle the words if needed
items40 = list(lesson_40_words.items())
random.shuffle(items40)
lesson_40_words = dict(items40)


lesson_41_words = {
    "complacent": "pleased with oneself; self-satisfied",
    "wasp": "an insect with a slender body and powerful sting",
    "rehabilitate": "restore to good condition; make over in a new form; restore to former standing, rank, reputation, etc.",
    "parole": "word of honor; conditional freedom; to free (a prisoner) under certain conditions",
    "vertical": "straight up and down with reference to the horizon, for example, a vertical line",
    "multitude": "a great number; a crowd",
    "nominate": "name as a candidate for office; appoint to an office",
    "potential": "possibility as opposed to actuality; capability of coming into being or action",
    "morgue": "place where bodies of unknown persons found dead are kept; the reference library of a newspaper office",
    "preoccupied": "took up all the attention",
    "upholstery": "coverings and cushions for furniture",
    "indifference": "lack of interest, care, or attention"
}

# Shuffle the words if needed
items41 = list(lesson_41_words.items())
random.shuffle(items41)
lesson_41_words = dict(items41)


lesson_42_words = {
    "maintain": "keep; keep up; carry on; uphold; support; declare to be true",
    "snub": "treat coldly, scornfully, or with contempt; cold treatment",
    "endure": "last; keep on; undergo; bear; stand",
    "wrath": "very great anger; rage",
    "expose": "lay open; uncover; leave unprotected; show openly",
    "legend": "story coming from the past, which many people have believed; what is written on a coin or below a picture",
    "ponder": "consider carefully",
    "resign": "give up; yield; submit",
    "drastic": "acting with force or violence",
    "wharf": "platform built on the shore or out from the shore beside which ships can load or unload",
    "amend": "change for the better; correct; change",
    "ballot": "piece of paper used in voting; the whole number of votes cast; the method of secret voting; to vote or decide by using ballots"
}

# Shuffle the words if needed
items42 = list(lesson_42_words.items())
random.shuffle(items42)
lesson_42_words = dict(items42)





lessons = {
    1: lesson_1_words,
    2: lesson_2_words,
    3: lesson_3_words,
    4: lesson_4_words,
    5: lesson_5_words,
    6: lesson_6_words,
    7: lesson_7_words,
    8: lesson_8_words,
    9: lesson_9_words,
    10: lesson_10_words,
    11: lesson_11_words,
    12: lesson_12_words,
    13: lesson_13_words,
    14: lesson_14_words,
    15: lesson_15_words,
    16: lesson_16_words,
    17: lesson_17_words,
    18: lesson_18_words,
    19: lesson_19_words,
    20: lesson_20_words,
    21: lesson_21_words,
    22: lesson_22_words,
    23: lesson_23_words,
    24: lesson_24_words,
    25: lesson_25_words,
    26: lesson_26_words,
    27: lesson_27_words,
    28: lesson_28_words,
    29: lesson_29_words,
    30: lesson_30_words,
    31: lesson_31_words,
    32: lesson_32_words,
    33: lesson_33_words,
    34: lesson_34_words,
    35: lesson_35_words,
    36: lesson_36_words,
    37: lesson_37_words,
    38: lesson_38_words,
    39: lesson_39_words,
    40: lesson_40_words,
    41: lesson_41_words,
    42: lesson_42_words,
}


@app.route('/')
def index():
    return render_template('index.html', lessons=lessons)

@app.route('/play', methods=['POST'])
def play():
    lesson_number = int(request.form['lesson'])
    lesson = lessons.get(lesson_number)
    if lesson:
        words = list(lesson.items())
        random.shuffle(words)
        return render_template('play.html', lesson_number=lesson_number, words=words[:12])
    else:
        return "Lesson not found"

@app.route('/result', methods=['POST'])
def result():
    lesson_number = int(request.form['lesson'])
    lesson = lessons.get(lesson_number)
    if lesson:
        user_answers = {word: request.form[word] for word in lesson.keys()}
        correct_answers = {word: definition for word, definition in lesson.items()}
        flag = {word: user_answers[word] == word for word in correct_answers.keys()}
        results = {word: (user_answers[word], definition) for word, definition in correct_answers.items()}
        return render_template('result.html', results=results, flag=flag)
    else:
        return "Lesson not found"
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
