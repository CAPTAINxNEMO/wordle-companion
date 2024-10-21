wordle_list = (
    'aback', 'abase', 'abate', 'abbey', 'abbot', 'abhor', 'abide', 'abled', 'abode', 'abort', 'about', 'above', 'abuse', 'abyss', 'acorn',
    'acrid', 'actor', 'acute', 'adage', 'adapt', 'adept', 'admin', 'admit', 'adobe', 'adopt', 'adore', 'adorn', 'adult', 'affix', 'afire',
    'afoot', 'afoul', 'after', 'again', 'agape', 'agate', 'agent', 'agile', 'aging', 'aglow', 'agony', 'agree', 'ahead', 'aider', 'aisle',
    'alarm', 'album', 'alert', 'algae', 'alibi', 'alien', 'align', 'alike', 'alive', 'allay', 'alley', 'allot', 'allow', 'alloy', 'aloft',
    'alone', 'along', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amaze', 'amber', 'amble', 'amend', 'amiss', 'amity', 'among',
    'ample', 'amply', 'amuse', 'angel', 'anger', 'angle', 'angry', 'angst', 'anime', 'ankle', 'annex', 'annoy', 'annul', 'anode', 'antic',
    'anvil', 'aorta', 'apart', 'aphid', 'aping', 'apnea', 'apple', 'apply', 'apron', 'aptly', 'arbor', 'ardor', 'arena', 'argue', 'arise',
    'armor', 'aroma', 'arose', 'array', 'arrow', 'arson', 'artsy', 'ascot', 'ashen', 'aside', 'askew', 'assay', 'asset', 'atoll', 'atone',
    'attic', 'audio', 'audit', 'augur', 'aunty', 'avail', 'avert', 'avian', 'avoid', 'await', 'awake', 'award', 'aware', 'awash', 'awful',
    'awoke', 'axial', 'axiom', 'axion', 'azure', 'bacon', 'badge', 'badly', 'bagel', 'baggy', 'baker', 'baler', 'balmy', 'banal', 'banjo',
    'barge', 'baron', 'basal', 'basic', 'basil', 'basin', 'basis', 'baste', 'batch', 'bathe', 'baton', 'batty', 'bawdy', 'bayou', 'beach',
    'beady', 'beard', 'beast', 'beech', 'beefy', 'befit', 'began', 'begat', 'beget', 'begin', 'begun', 'being', 'belch', 'belie', 'belle',
    'belly', 'below', 'bench', 'beret', 'berry', 'berth', 'beset', 'betel', 'bevel', 'bezel', 'bible', 'bicep', 'biddy', 'bigot', 'bilge',
    'billy', 'binge', 'bingo', 'biome', 'birch', 'birth', 'bison', 'bitty', 'black', 'blade', 'blame', 'bland', 'blank', 'blare', 'blast',
    'blaze', 'bleak', 'bleat', 'bleed', 'bleep', 'blend', 'bless', 'blimp', 'blind', 'blink', 'bliss', 'blitz', 'bloat', 'block', 'bloke',
    'blond', 'blood', 'bloom', 'blown', 'bluer', 'bluff', 'blunt', 'blurb', 'blurt', 'blush', 'board', 'boast', 'bobby', 'boney', 'bongo',
    'bonus', 'booby', 'boost', 'booth', 'booty', 'booze', 'boozy', 'borax', 'borne', 'bosom', 'bossy', 'botch', 'bough', 'boule', 'bound',
    'bowel', 'boxer', 'brace', 'braid', 'brain', 'brake', 'brand', 'brash', 'brass', 'brave', 'bravo', 'brawl', 'brawn', 'bread', 'break',
    'breed', 'briar', 'bribe', 'brick', 'bride', 'brief', 'brine', 'bring', 'brink', 'briny', 'brisk', 'broad', 'broil', 'broke', 'brood',
    'brook', 'broom', 'broth', 'brown', 'brunt', 'brush', 'brute', 'buddy', 'budge', 'buggy', 'bugle', 'build', 'built', 'bulge', 'bulky',
    'bully', 'bunch', 'bunny', 'burly', 'burnt', 'burst', 'bused', 'bushy', 'butch', 'butte', 'buxom', 'buyer', 'bylaw', 'cabal', 'cabby',
    'cabin', 'cable', 'cacao', 'cache', 'cacti', 'caddy', 'cadet', 'cagey', 'cairn', 'camel', 'cameo', 'canal', 'candy', 'canny', 'canoe',
    'canon', 'caper', 'caput', 'carat', 'cargo', 'carol', 'carry', 'carve', 'caste', 'catch', 'cater', 'catty', 'caulk', 'cause', 'cavil',
    'cease', 'cedar', 'cello', 'chafe', 'chaff', 'chain', 'chair', 'chalk', 'champ', 'chant', 'chaos', 'chard', 'charm', 'chart', 'chase',
    'chasm', 'cheap', 'cheat', 'check', 'cheek', 'cheer', 'chess', 'chest', 'chick', 'chide', 'chief', 'child', 'chili', 'chill', 'chime',
    'china', 'chirp', 'chock', 'choir', 'choke', 'chord', 'chore', 'chose', 'chuck', 'chump', 'chunk', 'churn', 'chute', 'cider', 'cigar',
    'cinch', 'circa', 'civic', 'civil', 'clack', 'claim', 'clamp', 'clang', 'clank', 'clash', 'clasp', 'class', 'clean', 'clear', 'cleat',
    'cleft', 'clerk', 'click', 'cliff', 'climb', 'cling', 'clink', 'cloak', 'clock', 'clone', 'close', 'cloth', 'cloud', 'clout', 'clove',
    'clown', 'cluck', 'clued', 'clump', 'clung', 'coach', 'coast', 'cobra', 'cocoa', 'colon', 'color', 'comet', 'comfy', 'comic', 'comma',
    'conch', 'condo', 'conic', 'copse', 'coral', 'corer', 'corny', 'couch', 'cough', 'could', 'count', 'coupe', 'court', 'coven', 'cover',
    'covet', 'covey', 'cower', 'coyly', 'crack', 'craft', 'cramp', 'crane', 'crank', 'crash', 'crass', 'crate', 'crave', 'crawl', 'craze',
    'crazy', 'creak', 'cream', 'credo', 'creed', 'creek', 'creep', 'creme', 'crepe', 'crept', 'cress', 'crest', 'crick', 'cried', 'crier',
    'crime', 'crimp', 'crisp', 'croak', 'crock', 'crone', 'crony', 'crook', 'cross', 'croup', 'crowd', 'crown', 'crude', 'cruel', 'crumb',
    'crump', 'crush', 'crust', 'crypt', 'cubic', 'cumin', 'curio', 'curly', 'curry', 'curse', 'curve', 'curvy', 'cutie', 'cyber', 'cycle',
    'cynic', 'daddy', 'daily', 'dairy', 'daisy', 'dally', 'dance', 'dandy', 'datum', 'daunt', 'dealt', 'death', 'debar', 'debit', 'debug',
    'debut', 'decal', 'decay', 'decor', 'decoy', 'decry', 'defer', 'deign', 'deity', 'delay', 'delta', 'delve', 'demon', 'demur', 'denim',
    'dense', 'depot', 'depth', 'derby', 'deter', 'detox', 'deuce', 'devil', 'diary', 'dicey', 'digit', 'dilly', 'dimly', 'diner', 'dingo',
    'dingy', 'diode', 'dirge', 'dirty', 'disco', 'ditch', 'ditto', 'ditty', 'diver', 'dizzy', 'dodge', 'dodgy', 'dogma', 'doing', 'dolly',
    'donor', 'donut', 'dopey', 'doubt', 'dough', 'dowdy', 'dowel', 'downy', 'dowry', 'dozen', 'draft', 'drain', 'drake', 'drama', 'drank',
    'drape', 'drawl', 'drawn', 'dread', 'dream', 'dress', 'dried', 'drier', 'drift', 'drill', 'drink', 'drive', 'droit', 'droll', 'drone',
    'drool', 'droop', 'dross', 'drove', 'drown', 'druid', 'drunk', 'dryer', 'dryly', 'duchy', 'dully', 'dummy', 'dumpy', 'dunce', 'dusky',
    'dusty', 'dutch', 'duvet', 'dwarf', 'dwell', 'dwelt', 'dying', 'eager', 'eagle', 'early', 'earth', 'easel', 'eaten', 'eater', 'ebony',
    'eclat', 'edict', 'edify', 'eerie', 'egret', 'eight', 'eject', 'eking', 'elate', 'elbow', 'elder', 'elect', 'elegy', 'elfin', 'elide',
    'elite', 'elope', 'elude', 'email', 'embed', 'ember', 'emcee', 'empty', 'enact', 'endow', 'enema', 'enemy', 'enjoy', 'ennui', 'ensue',
    'enter', 'entry', 'envoy', 'epoch', 'epoxy', 'equal', 'equip', 'erase', 'erect', 'erode', 'error', 'erupt', 'essay', 'ester', 'ether',
    'ethic', 'ethos', 'etude', 'evade', 'event', 'every', 'evict', 'evoke', 'exact', 'exalt', 'excel', 'exert', 'exile', 'exist', 'expel',
    'extol', 'extra', 'exult', 'eying', 'fable', 'facet', 'faint', 'fairy', 'faith', 'false', 'fancy', 'fanny', 'farce', 'fatal', 'fatty',
    'fault', 'fauna', 'favor', 'feast', 'fecal', 'feign', 'fella', 'felon', 'femme', 'femur', 'fence', 'feral', 'ferry', 'fetal', 'fetch',
    'fetid', 'fetus', 'fever', 'fewer', 'fiber', 'ficus', 'field', 'fiend', 'fiery', 'fifth', 'fifty', 'fight', 'filer', 'filet', 'filly',
    'filmy', 'filth', 'final', 'finch', 'finer', 'first', 'fishy', 'fixer', 'fizzy', 'fjord', 'flack', 'flail', 'flair', 'flake', 'flaky',
    'flame', 'flank', 'flare', 'flash', 'flask', 'fleck', 'fleet', 'flesh', 'flick', 'flier', 'fling', 'flint', 'flirt', 'float', 'flock',
    'flood', 'floor', 'flora', 'floss', 'flour', 'flout', 'flown', 'fluff', 'fluid', 'fluke', 'flume', 'flung', 'flunk', 'flush', 'flute',
    'flyer', 'foamy', 'focal', 'focus', 'foggy', 'foist', 'folio', 'folly', 'foray', 'force', 'forge', 'forgo', 'forte', 'forth', 'forty',
    'forum', 'found', 'foyer', 'frail', 'frame', 'frank', 'fraud', 'freak', 'freed', 'freer', 'fresh', 'friar', 'fried', 'frill', 'frisk',
    'fritz', 'frock', 'frond', 'front', 'frost', 'froth', 'frown', 'froze', 'fruit', 'fudge', 'fugue', 'fully', 'fungi', 'funky', 'funny',
    'furor', 'furry', 'fussy', 'fuzzy', 'gaffe', 'gaily', 'gamer', 'gamma', 'gamut', 'gassy', 'gaudy', 'gauge', 'gaunt', 'gauze', 'gavel',
    'gawky', 'gayer', 'gayly', 'gazer', 'gecko', 'geeky', 'geese', 'genie', 'genre', 'ghost', 'ghoul', 'giant', 'giddy', 'gipsy', 'girly',
    'girth', 'given', 'giver', 'glade', 'gland', 'glare', 'glass', 'glaze', 'gleam', 'glean', 'glide', 'glint', 'gloat', 'globe', 'gloom',
    'glory', 'gloss', 'glove', 'glyph', 'gnash', 'gnome', 'godly', 'going', 'golem', 'golly', 'gonad', 'goner', 'goody', 'gooey', 'goofy',
    'goose', 'gorge', 'gouge', 'gourd', 'grace', 'grade', 'graft', 'grail', 'grain', 'grand', 'grant', 'grape', 'graph', 'grasp', 'grass',
    'grate', 'grave', 'gravy', 'graze', 'great', 'greed', 'green', 'greet', 'grief', 'grill', 'grime', 'grimy', 'grind', 'gripe', 'groan',
    'groin', 'groom', 'grope', 'gross', 'group', 'grout', 'grove', 'growl', 'grown', 'gruel', 'gruff', 'grunt', 'guard', 'guava', 'guess',
    'guest', 'guide', 'guild', 'guile', 'guilt', 'guise', 'gulch', 'gully', 'gumbo', 'gummy', 'guppy', 'gusto', 'gusty', 'gypsy', 'habit',
    'hairy', 'halve', 'handy', 'happy', 'hardy', 'harem', 'harpy', 'harry', 'harsh', 'haste', 'hasty', 'hatch', 'hater', 'haunt', 'haute',
    'haven', 'havoc', 'hazel', 'heady', 'heard', 'heart', 'heath', 'heave', 'heavy', 'hedge', 'hefty', 'heist', 'helix', 'hello', 'hence',
    'heron', 'hilly', 'hinge', 'hippo', 'hippy', 'hitch', 'hoard', 'hobby', 'hoist', 'holly', 'homer', 'honey', 'honor', 'horde', 'horny',
    'horse', 'hotel', 'hotly', 'hound', 'house', 'hovel', 'hover', 'howdy', 'human', 'humid', 'humor', 'humph', 'humus', 'hunch', 'hunky',
    'hurry', 'husky', 'hussy', 'hutch', 'hydro', 'hyena', 'hymen', 'hyper', 'icily', 'icing', 'ideal', 'idiom', 'idiot', 'idler', 'idyll',
    'igloo', 'iliac', 'image', 'imbue', 'impel', 'imply', 'inane', 'inbox', 'incur', 'index', 'inept', 'inert', 'infer', 'ingot', 'inlay',
    'inlet', 'inner', 'input', 'inter', 'intro', 'ionic', 'irate', 'irony', 'islet', 'issue', 'itchy', 'ivory', 'jaunt', 'jazzy', 'jelly',
    'jerky', 'jetty', 'jewel', 'jiffy', 'joint', 'joist', 'joker', 'jolly', 'joust', 'judge', 'juice', 'juicy', 'jumbo', 'jumpy', 'junta',
    'junto', 'juror', 'kappa', 'karma', 'kayak', 'kebab', 'khaki', 'kinky', 'kiosk', 'kitty', 'knack', 'knave', 'knead', 'kneed', 'kneel',
    'knelt', 'knife', 'knock', 'knoll', 'known', 'koala', 'krill', 'label', 'labor', 'laden', 'ladle', 'lager', 'lance', 'lanky', 'lapel',
    'lapse', 'large', 'larva', 'lasso', 'latch', 'later', 'lathe', 'latte', 'laugh', 'layer', 'leach', 'leafy', 'leaky', 'leant', 'leapt',
    'learn', 'lease', 'leash', 'least', 'leave', 'ledge', 'leech', 'leery', 'lefty', 'legal', 'leggy', 'lemon', 'lemur', 'leper', 'level',
    'lever', 'libel', 'liege', 'light', 'liken', 'lilac', 'limbo', 'limit', 'linen', 'liner', 'lingo', 'lipid', 'lithe', 'liver', 'livid',
    'llama', 'loamy', 'loath', 'lobby', 'local', 'locus', 'lodge', 'lofty', 'logic', 'login', 'loopy', 'loose', 'lorry', 'loser', 'louse',
    'lousy', 'lover', 'lower', 'lowly', 'loyal', 'lucid', 'lucky', 'lumen', 'lumpy', 'lunar', 'lunch', 'lunge', 'lupus', 'lurch', 'lurid',
    'lusty', 'lying', 'lymph', 'lyric', 'macaw', 'macho', 'macro', 'madam', 'madly', 'mafia', 'magic', 'magma', 'maize', 'major', 'maker',
    'mambo', 'mamma', 'mammy', 'manga', 'mange', 'mango', 'mangy', 'mania', 'manic', 'manly', 'manor', 'maple', 'march', 'marry', 'marsh',
    'mason', 'masse', 'match', 'matey', 'mauve', 'maxim', 'maybe', 'mayor', 'mealy', 'meant', 'meaty', 'mecca', 'medal', 'media', 'medic',
    'melee', 'melon', 'mercy', 'merge', 'merit', 'merry', 'metal', 'meter', 'metro', 'micro', 'midge', 'midst', 'might', 'milky', 'mimic',
    'mince', 'miner', 'minim', 'minor', 'minty', 'minus', 'mirth', 'miser', 'missy', 'mocha', 'modal', 'model', 'modem', 'mogul', 'moist',
    'molar', 'moldy', 'money', 'month', 'moody', 'moose', 'moral', 'moron', 'morph', 'mossy', 'motel', 'motif', 'motor', 'motto', 'moult',
    'mound', 'mount', 'mourn', 'mouse', 'mouth', 'mover', 'movie', 'mower', 'mucky', 'mucus', 'muddy', 'mulch', 'mummy', 'munch', 'mural',
    'murky', 'mushy', 'music', 'musky', 'musty', 'myrrh', 'nadir', 'naive', 'nanny', 'nasal', 'nasty', 'natal', 'naval', 'navel', 'needy',
    'neigh', 'nerdy', 'nerve', 'never', 'newer', 'newly', 'nicer', 'niche', 'niece', 'night', 'ninja', 'ninny', 'ninth', 'noble', 'nobly',
    'noise', 'noisy', 'nomad', 'noose', 'north', 'nosey', 'notch', 'novel', 'nudge', 'nurse', 'nutty', 'nylon', 'nymph', 'oaken', 'obese',
    'occur', 'ocean', 'octal', 'octet', 'odder', 'oddly', 'offal', 'offer', 'often', 'olden', 'older', 'olive', 'ombre', 'omega', 'onion',
    'onset', 'opera', 'opine', 'opium', 'optic', 'orbit', 'order', 'organ', 'other', 'otter', 'ought', 'ounce', 'outdo', 'outer', 'outgo',
    'ovary', 'ovate', 'overt', 'ovine', 'ovoid', 'owing', 'owner', 'oxide', 'ozone', 'paddy', 'pagan', 'paint', 'paler', 'palsy', 'panel',
    'panic', 'pansy', 'papal', 'paper', 'parer', 'parka', 'parry', 'parse', 'party', 'pasta', 'paste', 'pasty', 'patch', 'patio', 'patsy',
    'patty', 'pause', 'payee', 'payer', 'peace', 'peach', 'pearl', 'pecan', 'pedal', 'penal', 'pence', 'penne', 'penny', 'perch', 'peril',
    'perky', 'pesky', 'pesto', 'petal', 'petty', 'phase', 'phone', 'phony', 'photo', 'piano', 'picky', 'piece', 'piety', 'piggy', 'pilot',
    'pinch', 'piney', 'pinky', 'pinto', 'piper', 'pique', 'pitch', 'pithy', 'pivot', 'pixel', 'pixie', 'pizza', 'place', 'plaid', 'plain',
    'plait', 'plane', 'plank', 'plant', 'plate', 'plaza', 'plead', 'pleat', 'plied', 'plier', 'pluck', 'plumb', 'plume', 'plump', 'plunk',
    'plush', 'poesy', 'point', 'poise', 'poker', 'polar', 'polka', 'polyp', 'pooch', 'poppy', 'porch', 'poser', 'posit', 'posse', 'pouch',
    'pound', 'pouty', 'power', 'prank', 'prawn', 'preen', 'press', 'price', 'prick', 'pride', 'pried', 'prime', 'primo', 'print', 'prior',
    'prism', 'privy', 'prize', 'probe', 'prone', 'prong', 'proof', 'prose', 'proud', 'prove', 'prowl', 'proxy', 'prude', 'prune', 'psalm',
    'pubic', 'pudgy', 'puffy', 'pulpy', 'pulse', 'punch', 'pupil', 'puppy', 'puree', 'purer', 'purge', 'purse', 'pushy', 'putty', 'pygmy',
    'quack', 'quail', 'quake', 'qualm', 'quark', 'quart', 'quash', 'quasi', 'queen', 'queer', 'quell', 'query', 'quest', 'queue', 'quick',
    'quiet', 'quill', 'quilt', 'quirk', 'quite', 'quota', 'quote', 'quoth', 'rabbi', 'rabid', 'racer', 'radar', 'radii', 'radio', 'rainy',
    'raise', 'rajah', 'rally', 'ralph', 'ramen', 'ranch', 'randy', 'range', 'rapid', 'rarer', 'raspy', 'ratio', 'ratty', 'raven', 'rayon',
    'razor', 'reach', 'react', 'ready', 'realm', 'rearm', 'rebar', 'rebel', 'rebus', 'rebut', 'recap', 'recur', 'recut', 'reedy', 'refer',
    'refit', 'regal', 'rehab', 'reign', 'relax', 'relay', 'relic', 'remit', 'renal', 'renew', 'repay', 'repel', 'reply', 'rerun', 'reset',
    'resin', 'retch', 'retro', 'retry', 'reuse', 'revel', 'revue', 'rhino', 'rhyme', 'rider', 'ridge', 'rifle', 'right', 'rigid', 'rigor',
    'rinse', 'ripen', 'riper', 'risen', 'riser', 'risky', 'rival', 'river', 'rivet', 'roach', 'roast', 'robin', 'robot', 'rocky', 'rodeo',
    'roger', 'rogue', 'roomy', 'roost', 'rotor', 'rouge', 'rough', 'round', 'rouse', 'route', 'rover', 'rowdy', 'rower', 'royal', 'ruddy',
    'ruder', 'rugby', 'ruler', 'rumba', 'rumor', 'rupee', 'rural', 'rusty', 'sadly', 'safer', 'saint', 'salad', 'sally', 'salon', 'salsa',
    'salty', 'salve', 'salvo', 'sandy', 'saner', 'sappy', 'sassy', 'satin', 'satyr', 'sauce', 'saucy', 'sauna', 'saute', 'savor', 'savoy',
    'savvy', 'scald', 'scale', 'scalp', 'scaly', 'scamp', 'scant', 'scare', 'scarf', 'scary', 'scene', 'scent', 'scion', 'scoff', 'scold',
    'scone', 'scoop', 'scope', 'score', 'scorn', 'scour', 'scout', 'scowl', 'scram', 'scrap', 'scree', 'screw', 'scrub', 'scrum', 'scuba',
    'sedan', 'seedy', 'segue', 'seize', 'semen', 'sense', 'sepia', 'serif', 'serum', 'serve', 'setup', 'seven', 'sever', 'sewer', 'shack',
    'shade', 'shady', 'shaft', 'shake', 'shaky', 'shale', 'shall', 'shalt', 'shame', 'shank', 'shape', 'shard', 'share', 'shark', 'sharp',
    'shave', 'shawl', 'shear', 'sheen', 'sheep', 'sheer', 'sheet', 'sheik', 'shelf', 'shell', 'shied', 'shift', 'shine', 'shiny', 'shire',
    'shirk', 'shirt', 'shoal', 'shock', 'shone', 'shook', 'shoot', 'shore', 'shorn', 'short', 'shout', 'shove', 'shown', 'showy', 'shrew',
    'shrub', 'shrug', 'shuck', 'shunt', 'shush', 'shyly', 'siege', 'sieve', 'sight', 'sigma', 'silky', 'silly', 'since', 'sinew', 'singe',
    'siren', 'sissy', 'sixth', 'sixty', 'skate', 'skier', 'skiff', 'skill', 'skimp', 'skirt', 'skulk', 'skull', 'skunk', 'slack', 'slain',
    'slang', 'slant', 'slash', 'slate', 'sleek', 'sleep', 'sleet', 'slept', 'slice', 'slick', 'slide', 'slime', 'slimy', 'sling', 'slink',
    'sloop', 'slope', 'slosh', 'sloth', 'slump', 'slung', 'slunk', 'slurp', 'slush', 'slyly', 'smack', 'small', 'smart', 'smash', 'smear',
    'smell', 'smelt', 'smile', 'smirk', 'smite', 'smith', 'smock', 'smoke', 'smoky', 'smote', 'snack', 'snail', 'snake', 'snaky', 'snare',
    'snarl', 'sneak', 'sneer', 'snide', 'sniff', 'snipe', 'snoop', 'snore', 'snort', 'snout', 'snowy', 'snuck', 'snuff', 'soapy', 'sober',
    'soggy', 'solar', 'solid', 'solve', 'sonar', 'sonic', 'sooth', 'sooty', 'sorry', 'sound', 'south', 'sower', 'space', 'spade', 'spank',
    'spare', 'spark', 'spasm', 'spawn', 'speak', 'spear', 'speck', 'speed', 'spell', 'spelt', 'spend', 'spent', 'sperm', 'spice', 'spicy',
    'spied', 'spiel', 'spike', 'spiky', 'spill', 'spilt', 'spine', 'spiny', 'spire', 'spite', 'splat', 'split', 'spoil', 'spoke', 'spoof',
    'spook', 'spool', 'spoon', 'spore', 'sport', 'spout', 'spray', 'spree', 'sprig', 'spunk', 'spurn', 'spurt', 'squad', 'squat', 'squib',
    'stack', 'staff', 'stage', 'staid', 'stain', 'stair', 'stake', 'stale', 'stalk', 'stall', 'stamp', 'stand', 'stank', 'stare', 'stark',
    'start', 'stash', 'state', 'stave', 'stead', 'steak', 'steal', 'steam', 'steed', 'steel', 'steep', 'steer', 'stein', 'stern', 'stick',
    'stiff', 'still', 'stilt', 'sting', 'stink', 'stint', 'stock', 'stoic', 'stoke', 'stole', 'stomp', 'stone', 'stony', 'stood', 'stool',
    'stoop', 'store', 'stork', 'storm', 'story', 'stout', 'stove', 'strap', 'straw', 'stray', 'strip', 'strut', 'stuck', 'study', 'stuff',
    'stump', 'stung', 'stunk', 'stunt', 'style', 'suave', 'sugar', 'suing', 'suite', 'sulky', 'sully', 'sumac', 'sunny', 'super', 'surer',
    'surge', 'surly', 'sushi', 'swami', 'swamp', 'swarm', 'swash', 'swath', 'swear', 'sweat', 'sweep', 'sweet', 'swell', 'swept', 'swift',
    'swill', 'swine', 'swing', 'swirl', 'swish', 'swoon', 'swoop', 'sword', 'swore', 'sworn', 'swung', 'synod', 'syrup', 'tabby', 'table',
    'taboo', 'tacit', 'tacky', 'taffy', 'taint', 'taken', 'taker', 'tally', 'talon', 'tamer', 'tango', 'tangy', 'taper', 'tapir', 'tardy',
    'tarot', 'taste', 'tasty', 'tatty', 'taunt', 'tawny', 'teach', 'teary', 'tease', 'teddy', 'teeth', 'tempo', 'tenet', 'tenor', 'tense',
    'tenth', 'tepee', 'tepid', 'terra', 'terse', 'testy', 'thank', 'theft', 'their', 'theme', 'there', 'these', 'theta', 'thick', 'thief',
    'thigh', 'thing', 'think', 'third', 'thong', 'thorn', 'those', 'three', 'threw', 'throb', 'throw', 'thrum', 'thumb', 'thump', 'thyme',
    'tiara', 'tibia', 'tidal', 'tiger', 'tight', 'tilde', 'timer', 'timid', 'tipsy', 'titan', 'tithe', 'title', 'toast', 'today', 'toddy',
    'token', 'tonal', 'tonga', 'tonic', 'tooth', 'topaz', 'topic', 'torch', 'torso', 'torus', 'total', 'totem', 'touch', 'tough', 'towel',
    'tower', 'toxic', 'toxin', 'trace', 'track', 'tract', 'trade', 'trail', 'train', 'trait', 'tramp', 'trash', 'trawl', 'tread', 'treat',
    'trend', 'triad', 'trial', 'tribe', 'trice', 'trick', 'tried', 'tripe', 'trite', 'troll', 'troop', 'trope', 'trout', 'trove', 'truce',
    'truck', 'truer', 'truly', 'trump', 'trunk', 'truss', 'trust', 'truth', 'tryst', 'tubal', 'tuber', 'tulip', 'tulle', 'tumor', 'tunic',
    'turbo', 'tutor', 'twang', 'tweak', 'tweed', 'tweet', 'twice', 'twine', 'twirl', 'twist', 'twixt', 'tying', 'udder', 'ulcer', 'ultra',
    'umbra', 'uncle', 'uncut', 'under', 'undid', 'undue', 'unfed', 'unfit', 'unify', 'union', 'unite', 'unity', 'unlit', 'unmet', 'unset',
    'untie', 'until', 'unwed', 'unzip', 'upper', 'upset', 'urban', 'urine', 'usage', 'usher', 'using', 'usual', 'usurp', 'utile', 'utter',
    'vague', 'valet', 'valid', 'valor', 'value', 'valve', 'vapid', 'vapor', 'vault', 'vaunt', 'vegan', 'venom', 'venue', 'verge', 'verse',
    'verso', 'verve', 'vicar', 'video', 'vigil', 'vigor', 'villa', 'vinyl', 'viola', 'viper', 'viral', 'virus', 'visit', 'visor', 'vista',
    'vital', 'vivid', 'vixen', 'vocal', 'vodka', 'vogue', 'voice', 'voila', 'vomit', 'voter', 'vouch', 'vowel', 'vying', 'wacky', 'wafer',
    'wager', 'wagon', 'waist', 'waive', 'waltz', 'warty', 'waste', 'watch', 'water', 'waver', 'waxen', 'weary', 'weave', 'wedge', 'weedy',
    'weigh', 'weird', 'welch', 'welsh', 'whack', 'whale', 'wharf', 'wheat', 'wheel', 'whelp', 'where', 'which', 'whiff', 'while', 'whine',
    'whiny', 'whirl', 'whisk', 'white', 'whole', 'whoop', 'whose', 'widen', 'wider', 'widow', 'width', 'wield', 'wight', 'willy', 'wimpy',
    'wince', 'winch', 'windy', 'wiser', 'wispy', 'witch', 'witty', 'woken', 'woman', 'women', 'woody', 'wooer', 'wooly', 'woozy', 'wordy',
    'world', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'woven', 'wrack', 'wrath', 'wreak', 'wreck', 'wrest', 'wring', 'wrist',
    'write', 'wrong', 'wrote', 'wrung', 'wryly', 'yacht', 'yearn', 'yeast', 'yield', 'young', 'youth', 'zebra', 'zesty', 'zonal'
)

past_solutions = (
    'aback', 'abase', 'abate', 'abbey', 'abide', 'about', 'above', 'abyss', 'acorn', 'acrid', 'actor', 'acute', 'adage', 'adapt', 'admit',
    'adobe', 'adopt', 'adore', 'adult', 'after', 'again', 'agape', 'agate', 'agent', 'agile', 'aging', 'aglow', 'agony', 'agree', 'ahead',
    'aisle', 'album', 'alien', 'alike', 'alive', 'allow', 'aloft', 'alone', 'aloof', 'aloud', 'alpha', 'altar', 'alter', 'amass', 'amber',
    'amiss', 'ample', 'angel', 'anger', 'angry', 'angst', 'anode', 'antic', 'anvil', 'aorta', 'apart', 'aphid', 'apple', 'apply', 'apron',
    'aptly', 'arbor', 'ardor', 'argue', 'aroma', 'ascot', 'aside', 'askew', 'asset', 'atoll', 'atone', 'audio', 'audit', 'avail', 'avert',
    'await', 'awake', 'awash', 'awful', 'axiom', 'azure', 'bacon', 'badge', 'badly', 'bagel', 'baker', 'balsa', 'banal', 'barge', 'basic',
    'basin', 'bathe', 'baton', 'batty', 'bayou', 'beach', 'beady', 'beast', 'beaut', 'beefy', 'beget', 'begin', 'being', 'belch', 'belie',
    'belly', 'below', 'bench', 'beret', 'berth', 'beset', 'bevel', 'binge', 'biome', 'birch', 'birth', 'black', 'blame', 'bland', 'blare',
    'bleak', 'bleed', 'bleep', 'blimp', 'block', 'bloke', 'blond', 'blown', 'bluff', 'blurb', 'blurt', 'blush', 'booby', 'boost', 'booze',
    'boozy', 'borax', 'bough', 'brace', 'braid', 'brain', 'brake', 'brash', 'brass', 'brave', 'bravo', 'bread', 'break', 'breed', 'briar',
    'bribe', 'bride', 'brief', 'brine', 'bring', 'brink', 'briny', 'brisk', 'broad', 'broke', 'brook', 'broom', 'broth', 'brush', 'brute',
    'buddy', 'buggy', 'bugle', 'build', 'built', 'bulky', 'bully', 'bunch', 'burly', 'cable', 'cacao', 'cache', 'cadet', 'camel', 'cameo',
    'candy', 'canny', 'canoe', 'canon', 'caper', 'carat', 'cargo', 'carol', 'carry', 'carve', 'catch', 'cater', 'caulk', 'cause', 'cedar',
    'chafe', 'chain', 'chalk', 'champ', 'chant', 'chaos', 'chard', 'charm', 'chart', 'cheat', 'cheek', 'cheer', 'chest', 'chief', 'child',
    'chill', 'chime', 'choir', 'choke', 'chord', 'chunk', 'chute', 'cider', 'cigar', 'cinch', 'circa', 'civic', 'class', 'clean', 'clear',
    'cleft', 'clerk', 'click', 'climb', 'cling', 'clock', 'clone', 'close', 'cloth', 'cloud', 'clown', 'cluck', 'coach', 'coast', 'cocoa',
    'colon', 'comet', 'comma', 'condo', 'conic', 'corer', 'corny', 'could', 'count', 'court', 'cover', 'covet', 'cower', 'coyly', 'craft',
    'cramp', 'crane', 'crank', 'crass', 'crate', 'crave', 'craze', 'crazy', 'creak', 'credo', 'crept', 'crime', 'crimp', 'croak', 'crone',
    'cross', 'crowd', 'crown', 'crumb', 'crush', 'crust', 'cumin', 'curly', 'cynic', 'daddy', 'daisy', 'dance', 'dandy', 'death', 'debit',
    'debug', 'debut', 'decal', 'decay', 'decoy', 'delay', 'delta', 'delve', 'denim', 'depot', 'depth', 'deter', 'devil', 'diary', 'digit',
    'diner', 'dingo', 'disco', 'ditto', 'dodge', 'doing', 'dolly', 'donor', 'donut', 'doubt', 'dowry', 'dozen', 'drain', 'drawn', 'dream',
    'drink', 'drive', 'droll', 'droop', 'drove', 'duchy', 'dutch', 'duvet', 'dwarf', 'dwell', 'dwelt', 'early', 'earth', 'ebony', 'edict',
    'egret', 'eject', 'elder', 'elope', 'elude', 'email', 'ember', 'empty', 'enact', 'enema', 'enjoy', 'ennui', 'ensue', 'enter', 'epoch',
    'epoxy', 'equal', 'equip', 'erode', 'error', 'erupt', 'essay', 'ether', 'ethic', 'ethos', 'evade', 'every', 'evoke', 'exact', 'exalt',
    'excel', 'exert', 'exist', 'expel', 'extra', 'exult', 'facet', 'faint', 'faith', 'farce', 'fault', 'favor', 'feast', 'feign', 'feral',
    'ferry', 'fewer', 'field', 'fiend', 'fifty', 'filet', 'final', 'finch', 'finer', 'first', 'fishy', 'fixer', 'fjord', 'flail', 'flair',
    'flake', 'flame', 'flank', 'flare', 'flask', 'flesh', 'flick', 'fling', 'flirt', 'float', 'flock', 'flood', 'floor', 'flora', 'floss',
    'flour', 'flout', 'fluff', 'flume', 'flunk', 'flyer', 'focal', 'focus', 'foggy', 'folly', 'foray', 'force', 'forge', 'forgo', 'forte',
    'forth', 'forty', 'found', 'foyer', 'frame', 'frank', 'fresh', 'fried', 'frock', 'frond', 'front', 'frost', 'froth', 'froze', 'fully',
    'fungi', 'funny', 'gamer', 'gamma', 'gamut', 'gaudy', 'gaunt', 'gauze', 'gawky', 'gecko', 'genre', 'ghoul', 'giant', 'giddy', 'girth',
    'given', 'glass', 'glaze', 'gleam', 'glean', 'glide', 'gloat', 'globe', 'gloom', 'glory', 'glove', 'glyph', 'gnash', 'golem', 'goner',
    'goose', 'gorge', 'gouge', 'grace', 'grade', 'grail', 'grand', 'grant', 'graph', 'grasp', 'grate', 'great', 'green', 'greet', 'grief',
    'grime', 'grimy', 'grind', 'gripe', 'groin', 'groom', 'group', 'grout', 'grove', 'growl', 'gruel', 'guano', 'guard', 'guest', 'guide',
    'guild', 'gully', 'gummy', 'guppy', 'gusty', 'hairy', 'halve', 'handy', 'happy', 'harsh', 'hatch', 'hater', 'havoc', 'heady', 'heard',
    'heart', 'heath', 'heave', 'heavy', 'heist', 'helix', 'hello', 'hence', 'heron', 'hinge', 'hitch', 'hoard', 'hobby', 'homer', 'honey',
    'horde', 'horse', 'hotel', 'hound', 'house', 'howdy', 'human', 'humid', 'humor', 'humph', 'hunch', 'hunky', 'hurry', 'hutch', 'hyper',
    'igloo', 'image', 'impel', 'inane', 'index', 'inept', 'inert', 'infer', 'inlay', 'input', 'inter', 'intro', 'ionic', 'irate', 'irony',
    'islet', 'itchy', 'ivory', 'jaunt', 'jazzy', 'jerky', 'jiffy', 'joint', 'joker', 'jolly', 'joust', 'judge', 'juice', 'karma', 'kayak',
    'kazoo', 'kebab', 'khaki', 'kiosk', 'knave', 'knead', 'kneel', 'knelt', 'knock', 'knoll', 'koala', 'label', 'labor', 'lager', 'lanky',
    'lapel', 'lapse', 'large', 'larva', 'laser', 'latte', 'layer', 'leafy', 'leaky', 'leapt', 'learn', 'leash', 'leave', 'ledge', 'leech',
    'leery', 'leggy', 'lemon', 'libel', 'light', 'lilac', 'limit', 'linen', 'liner', 'lingo', 'lithe', 'liver', 'local', 'locus', 'lofty',
    'logic', 'loopy', 'loser', 'louse', 'lover', 'lower', 'lowly', 'loyal', 'lucid', 'lucky', 'lunar', 'lunch', 'lunge', 'lusty', 'lying',
    'macaw', 'madam', 'magic', 'magma', 'maize', 'major', 'mania', 'manga', 'manly', 'manor', 'maple', 'march', 'marry', 'marsh', 'mason',
    'masse', 'match', 'matey', 'maxim', 'maybe', 'mayor', 'mealy', 'meant', 'medal', 'media', 'medic', 'melon', 'mercy', 'merge', 'merit',
    'merry', 'metal', 'meter', 'metro', 'micro', 'midge', 'midst', 'mimic', 'mince', 'miner', 'minus', 'model', 'modem', 'moist', 'molar',
    'mommy', 'money', 'month', 'moose', 'mossy', 'motor', 'motto', 'moult', 'mount', 'mourn', 'mouse', 'movie', 'mucky', 'mulch', 'mummy',
    'mural', 'mushy', 'music', 'musty', 'naive', 'nanny', 'nasty', 'natal', 'naval', 'needy', 'neigh', 'nerdy', 'never', 'nicer', 'night',
    'ninja', 'ninth', 'noble', 'noise', 'north', 'nymph', 'occur', 'ocean', 'offal', 'often', 'older', 'olive', 'onion', 'onset', 'opera',
    'order', 'organ', 'other', 'ought', 'ounce', 'outdo', 'outer', 'overt', 'owner', 'oxide', 'paint', 'panel', 'panic', 'papal', 'paper',
    'parer', 'parry', 'party', 'pasta', 'patty', 'pause', 'peace', 'peach', 'penne', 'perch', 'perky', 'pesky', 'phase', 'phone', 'phony',
    'photo', 'piano', 'picky', 'piety', 'pilot', 'pinch', 'piney', 'pinky', 'pinto', 'pious', 'piper', 'pique', 'pithy', 'pixel', 'pixie',
    'place', 'plait', 'plank', 'plant', 'plate', 'plaza', 'pleat', 'pluck', 'plunk', 'point', 'poise', 'poker', 'polka', 'polyp', 'porch',
    'pound', 'power', 'press', 'price', 'prick', 'pride', 'prime', 'primo', 'print', 'prior', 'prize', 'probe', 'prone', 'prong', 'proud',
    'prove', 'prowl', 'proxy', 'prune', 'psalm', 'pulpy', 'purge', 'qualm', 'quart', 'queen', 'query', 'quest', 'queue', 'quick', 'quiet',
    'quirk', 'quite', 'quote', 'radio', 'rainy', 'raise', 'ramen', 'ranch', 'range', 'ratio', 'rayon', 'react', 'realm', 'rebel', 'rebus',
    'rebut', 'recap', 'recur', 'refer', 'regal', 'relic', 'renew', 'repay', 'repel', 'rerun', 'resin', 'retch', 'retro', 'retry', 'revel',
    'rhino', 'rhyme', 'ridge', 'rider', 'right', 'riper', 'risen', 'rival', 'robin', 'robot', 'rocky', 'rodeo', 'rogue', 'roomy', 'rouge',
    'round', 'rouse', 'route', 'rover', 'royal', 'ruddy', 'ruder', 'rupee', 'rusty', 'saint', 'salad', 'sally', 'salsa', 'salty', 'sassy',
    'saucy', 'saute', 'savor', 'scald', 'scale', 'scant', 'scare', 'scarf', 'scent', 'scoff', 'scold', 'scone', 'scope', 'scorn', 'scour',
    'scout', 'scram', 'scrap', 'scrub', 'sedan', 'seedy', 'sense', 'serum', 'serve', 'seven', 'sever', 'shade', 'shaft', 'shake', 'shall',
    'shame', 'shank', 'shape', 'shard', 'sharp', 'shave', 'shawl', 'shell', 'shift', 'shine', 'shire', 'shirk', 'shore', 'shorn', 'shown',
    'showy', 'shrub', 'shrug', 'shyly', 'siege', 'sight', 'since', 'sissy', 'skate', 'skier', 'skiff', 'skill', 'skimp', 'skirt', 'skunk',
    'slate', 'sleek', 'sleep', 'slice', 'slope', 'slosh', 'sloth', 'slump', 'slung', 'small', 'smart', 'smash', 'smear', 'smelt', 'smile',
    'smirk', 'smite', 'smith', 'smock', 'smoke', 'snack', 'snafu', 'snail', 'snake', 'snaky', 'snare', 'snarl', 'sneak', 'snort', 'snout',
    'soggy', 'solar', 'solid', 'solve', 'sonic', 'sound', 'sower', 'space', 'spade', 'speak', 'speck', 'spell', 'spelt', 'spend', 'spent',
    'spice', 'spicy', 'spiel', 'spike', 'spill', 'spire', 'splat', 'spoke', 'spout', 'spray', 'spurt', 'squad', 'squat', 'staff', 'stage',
    'staid', 'stain', 'stair', 'stake', 'stale', 'stall', 'stand', 'stark', 'start', 'stash', 'state', 'stead', 'steam', 'steed', 'steel',
    'stein', 'stern', 'stick', 'stiff', 'still', 'sting', 'stink', 'stint', 'stock', 'stole', 'stomp', 'stone', 'stony', 'stool', 'store',
    'storm', 'story', 'stout', 'stove', 'strap', 'straw', 'study', 'stung', 'style', 'sugar', 'sulky', 'super', 'surer', 'surly', 'sushi',
    'sweat', 'sweep', 'sweet', 'swill', 'swine', 'swirl', 'swish', 'swoon', 'swung', 'syrup', 'table', 'taboo', 'tacit', 'taken', 'talon',
    'tangy', 'taper', 'tapir', 'tardy', 'taste', 'tasty', 'taunt', 'tawny', 'teach', 'teary', 'tease', 'tempo', 'tenth', 'tepid', 'terse',
    'thank', 'their', 'theme', 'there', 'these', 'thief', 'thigh', 'thing', 'think', 'third', 'thorn', 'those', 'three', 'threw', 'throw',
    'thumb', 'thump', 'thyme', 'tiara', 'tibia', 'tidal', 'tiger', 'tilde', 'tipsy', 'titan', 'tithe', 'title', 'today', 'tonic', 'topaz',
    'topic', 'torch', 'torso', 'totem', 'touch', 'tough', 'towel', 'toxic', 'toxin', 'trace', 'tract', 'trade', 'train', 'trait', 'trash',
    'trawl', 'treat', 'trend', 'triad', 'trice', 'trite', 'troll', 'trope', 'trove', 'truss', 'trust', 'truth', 'tryst', 'tutor', 'twang',
    'tweak', 'tweed', 'twice', 'twine', 'twirl', 'ulcer', 'ultra', 'uncle', 'under', 'undue', 'unfed', 'unfit', 'unify', 'unite', 'unlit',
    'unmet', 'untie', 'until', 'unzip', 'upset', 'urban', 'usage', 'usher', 'using', 'usual', 'usurp', 'utter', 'vague', 'valet', 'valid',
    'value', 'vapid', 'vault', 'venom', 'verge', 'verve', 'video', 'vigor', 'viola', 'viral', 'vital', 'vivid', 'vodka', 'voice', 'voila',
    'voter', 'vouch', 'wacky', 'wagon', 'waltz', 'waste', 'watch', 'weary', 'wedge', 'whack', 'whale', 'wheel', 'whelp', 'where', 'which',
    'whiff', 'while', 'whine', 'whiny', 'whirl', 'whisk', 'whoop', 'widen', 'wince', 'windy', 'woken', 'woman', 'wooer', 'wordy', 'world',
    'worry', 'worse', 'worst', 'would', 'woven', 'wrath', 'wrist', 'write', 'wrong', 'wrote', 'wrung', 'yacht', 'yearn', 'yield', 'young',
    'youth', 'zebra', 'zesty', 'fiber', 'dicey', 'spoon', 'shout'
)

def get_gray_letters():
    gray_letters = set()
    gray_input = input('Gray letters (space-separated): ').lower()
    gray_letters = set(
        letter.strip()
        for letter in gray_input.split(' ')
        if letter.strip()
    )
    return gray_letters

def get_yellow_letters():
    yellow_letters = dict()
    print('Yellow Letters:')
    for position in range(5):
        while True:
            yellow_input = input(f'Position {position + 1} (space-separated, or leave blank if none): ').lower()
            if yellow_input == '':
                yellow_letters[position] = set()
                break
            elif all(
                char.isalpha()
                or char == ' '
                for char in yellow_input
            ):
                letters = set(
                    letter.strip()
                    for letter in yellow_input.split(' ')
                    if letter.strip()
                )
                if len(letters) > 0:
                    yellow_letters[position] = letters
                    break
                else:
                    print('Invalid input. Please enter at least one letter.')
            else:
                print('Invalid input. Please enter space-separated letters or leave blank.')
    return yellow_letters

def get_green_letters():
    green_letters = dict()
    print('Green Letters:')
    for position in range(5):
        while True:
            green_input = input(f'Position {position + 1} (or leave blank if none): ').lower()
            if green_input == '':
                green_letters[position] = None
                break
            elif green_input.isalpha() and len(green_input) == 1:
                green_letters[position] = green_input
                break
            else:
                print('Invalid input. Please enter a single letter or leave blank.')
    return green_letters

def filter_words(wordle_list, past_solutions, gray_letters, yellow_letters, green_letters):
    filtered_words = [
        word for word in wordle_list
        if not any(
            letter in word
            for letter in gray_letters
        )
        and all(
            word[i] in green_letters[i]
            for i in range(5)
            if green_letters[i]
        )
        and all(
            any(
                yellow_char in word
                and word[i] != yellow_char
                for yellow_char in yellow_letter
            )
            for i in range(5) if yellow_letters[i]
            for yellow_letter in yellow_letters[i]
        )
        and word not in past_solutions
    ]
    return filtered_words

if __name__ == '__main__':
    gray_letters = get_gray_letters()
    yellow_letters = get_yellow_letters()
    green_letters = get_green_letters()

    print('Possible Words:')
    filtered_words = filter_words(wordle_list, past_solutions, gray_letters, yellow_letters, green_letters)
    for i, word in enumerate(filtered_words):
        print(f'{i + 1}. {word}')
