# Morning Cats: A text-adventure game in Python
#
# Runs in Python 2.7
# Originally by redlandcannibal
# Last updated: 2014 April 2
# http://maestoso.org

from sys import exit

def start():
	print """
You are violently woken by what feels like a punch to your gut,
but is actually a massive grey cat jumping onto your stomach.
He settles on your chest, his enormous weight shoving the air out
of your lungs. He folds his little grey paws under him and peers
intensely into your sleepy, half-opened eyes. He licks his lips,
a look of indignant expectation on his face. It's pretty clear
that he wants you to wake up and feed him.
	
Will you wake up, or sleep?"""
	
	enter = raw_input("> ")
	
	if "wake" in enter:
		hallway()
	elif "sleep" in enter:
		badend("""
The boss cat calmly settles down on top of your windpipe. He ignores
your struggles and smirks as your life is slowly extinguished.""")
	else:
		print """
I don't know what '%s' means. Try \"wake up\" or \"sleep\".
""" % enter
		start()
		

def hallway():
	print """
You pull yourself out of the extremely comfortable bed and stumble
blearily into the hallway. The grey cat eagerly leaps after you and
meows expectantly. Just as you are about to turn the kitchen door
handle, a streak of black comes hurtling towards your legs.

What will you do?"""
	
	enter = raw_input("> ")
	
	if "dodge" in enter:
		kitchen()
	elif "kick" in enter:
		badend("""
You instinctively kick out. Your foot connects with a tiny, yowling
black cat. Enraged at being kicked, the black cat claws its way up
your leg. You see a flash of bright white teeth before your face is
forcibly removed from your skull.""")
	else:
		badend("""
The black blur turns out to be another cat, who knocks into your legs
and sends you flying. You catch a glimpse of the two cats doing epic
battle just before you pass out.""")
		

def kitchen():
	print """
You quickly dodge out of the way while the black streak collides
heavily into the wall. It turns out to be yet another cat, hungry for
breakfast and maybe your blood. You throw open the door to the
kitchen the exact instant the two cats hurl themselves at you."""
	forkintheroad()
	
def forkintheroad():
	print """
To your left is a living room with a big squashy couch and an HDTV.
To the right is your office, which is doubling as the cats' room.
It's a hollowed-out, desolate wasteland filled with shredded cat toys
and tumble weeds made of cat hair. You can see a crate of cat food
near what was once your desk, but is now a hair-covered cat palace.
Beside it are two crusty food bowls.

Will you enter the living room or the office?"""
	cats_fed = False
	
	while True:
		enter = raw_input("> ")
	
		if "office" in enter and not cats_fed:
			print """
You bob and weave your way through the myriad of claws and hairballs
and pry the lid off of the food tank just as the cats engage their
SUPER HYPER BERSERKER CAT FEEDING FRENZY mode.

Will you feed the cats, or flee from the madness?"""
			
			enter = raw_input("> ")
			if "feed" in enter:
				print """
You grab the two food bowls and dole out two hearty scoops of cat
food into each. The two cats weave furiously around and between your
legs, trying to get at the food. You place the bowls on the floor and
immediately withdraw your hands, lest they disappear in the ensuing
carnage. The cats, satisfied for now, settle on their haunches and
begin eating.

You make it back to the kitchen. The living room should be available
to you now that the cats are out of the way.

Will you enter the living room or go back to the office?"""
				cats_fed = True
			elif "flee" in enter:
				badend ("""
You make a mad dash out of the office and back to the hallway. As you
make a mad dash for the exit, a cat paw snakes around your ankle and
trips you up. Two sets of gleaming, grinning teeth bob in the air
above you as your vision fades to black.""")
			else:
				badend ("""
The cats, sensing weakness, lunge at the lid. It falls off with a
clatter, and the feeding frenzy has begun. When you reach out to stop
the cats from licking the whole bin clean, a smart cat-punch to the
temple knocks you unconscious. You black out to the sounds of two
cats horfing down an entire month's supply of cat food.""")
			
		elif "living" in enter and cats_fed:
			livingroom()
				
		elif "office" in enter and cats_fed == True:
			badend("""
			
The cats hear you enter the office and, still in berserker mode due
to the feeding frenzy, mistake you for a rival come to steal their
sustenance away. Before you can raise your hands to protect yourself,
you find that your arms are weighed down on both sides by fuzzy,
adorable little creatures who wish only to murder you.""")
			
		else:
			badend("""
The cats are disappointed in you. Their cold, glacial stares seem to
bore straight into your soul, and the shrill, wavering \"FEED ME\"
yowls pierce through your skull. Before you can take another step, a
huge weight falls on your chest and knocks you on your back. Two
fuzzy snouts push their way into your field of vision just as
everything fades to black.""")

		
	else:
		badend("""
You hesitate a moment too long. The cats are not pleased with your
indecision, and take it out by lovingly smothering your breathing
holes with their squishy, fuzzy bodies.""")

def livingroom():
	print """
You are finally able to sink your tired, weary body into the inviting
folds of your beloved sofa. You are able to grab the TV remote and
switch to the morning news when you suddenly year a yowl coming from
the office. The cats, left to their own primal devices, have started
fighting over the last scraps of food clinging to the bottom of their
bowls. Through the crack in the door that leads to the office you can
see what looks like a furry, dramatic reenactment of 300.

Do you watch the news, or do you check on the cats?"""

	enter = raw_input("> ")
		
	if "news" in enter:
		badend("""
The floorboards beneath you jump and quiver as your office struggles
to contain the epic cat battle. You try to tune it all out and turn
up the volume on your television to max. Right when the screen
switches to the weather report, you are suddenly enveloped in an
enormous pillar of light and energy. The realization crosses your
mind that you have been caught in the crossfire of one of the cats'
Neo Armstrong Cyclone Jet Armstrong Cannon blast crosses your mind.
Nanoseconds later, both you and your apartment are evaporated.""")
	elif "cats" in enter:
		goodend("""
The cats immediately settle down when you stand threateningly in the
doorway of the office. You are perilously sleep-deprived. It seems
like you can physically feel the tattered remains of your sanity and
patience ebb away.

Just as you are about to finally snap, the cats calmly wind
themselves around your feet, yawn hugely, and fall asleep. The
adorable sight of two sets of tiny paws resting on your toes is
almost too much to bear.

You take in a huge breath, let it all out in one ragged sigh, and
reach down to pat these adorable little dudes. They are UNBELIEVABLY
selfish and needy, but these moments of warm fuzzy cuteness make it
all worth it... right? ....... right?!""")
	else:
		print """
I don't know what '%s' means. Try \"news\" or \"cats\".
""" % enter

def badend(why):
	print why, "\n\n\n\t\t\tGAME OVER.\nTry again? Y/N"
	enter = raw_input("> ")
	
	if "Y" in enter:
		start()
	
	elif "y" in enter:
		start()
	
	else: 
		exit(0)
	
def goodend(why):
	print why, "\n\n\n\t\t\tYOU DID IT!\n"
	exit(0)
	
start()
