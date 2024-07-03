# Claude Agents

This repository contains code that puts two or more instances of very simple Claude "agents" to talk to each other. With the default settings the agents act as a shopkeeper of an ice cream truck and a customer.

To run, please install the dependencies (anthropic SDK) and run main.py.

The goal was to learn how anthropic SDK works, the effect of the system prompt, to see whether the agents could maintain a conversation, and to have fun.

# Example Output

><b>Shopkeeper</b>: <em>Ooh, 'ello there, young sir or madam! Welcome to me 'umble ice cream truck. What can I tempt you with on this scorching day? We've got yer vanilla, yer chocolate, yer strawberry - all the classics. Or if yer feeling adventurous, might I suggest our new flavor - tax-deductible tutti-frutti? It's a steal at only twice the price! Now, what'll it be?</em><br><br>
><b>Customer</b>: <em>Oh, splendid, just splendid. An ice cream truck with all of three flavors. How terribly innovative. I suppose next you'll be telling me you've got water in liquid form as well? Look, it's hotter than the devil's kitchen out here, and I'm positively melting. I don't suppose you could possibly manage to serve me something before the next ice age, could you? Or is that too much to ask? Come on, man, chop chop! I'll have a vanilla. No, wait, chocolate. Oh, good Lord, surprise me. Just make it quick before I turn into a puddle right here on the pavement!</em><br><br>
<b>Shopkeeper</b>: <em>Oh, I do beg yer pardon, Your Majesty! I didn't realize we 'ad royalty gracing our 'umble establishment today. You're right, of course - three flavors is a bit limited. Tell you what, why don't I whip up a special concoction just for you? I call it the "Impatient Patron's Delight." It's a scoop of each flavor, topped with a sprinkle of sarcasm and a cherry of me undyin' gratitude for yer custom. 
<br>
Now, while I prepare this masterpiece, perhaps you'd like to cool down by standin' in the shadow of yer own ego? It seems more than ample for the job! There we are, one "Impatient Patron's Delight" comin' right up. That'll be triple the usual price, on account of the rush job and the free comedy show you've been treatin' us all to. Cash or card?</em><br><br>
<b>Customer</b>: <em>Triple the price? Oh, how marvelous! Why don't you just take my firstborn child while you're at it? Perhaps I could sign over the deed to my house as well? I mean, it's not as if I need shelter when I can simply live in this ice cream cone you've so generously bestowed upon me. 
<br>
And what's this "Impatient Patron's Delight"? Sounds like something you'd scrape off the bottom of your freezer after a power outage. I asked for ice cream, not a culinary catastrophe! But fine, FINE! I'll take your overpriced, over-complicated frozen monstrosity. Anything to escape this heat and your attempts at wit. Now, let's see... I seem to have left my solid gold credit card in my other pants. Will you accept a cheque drawn on the Bank of Sarcasm?</em><br><br>
<b>Shopkeeper</b>: <em>Oh, a cheque from the Bank of Sarcasm? That's me favorite! I'll just file that right next to me collection of unicorn hair and pixie dust, shall I? Now, now, don't you worry about yer firstborn or yer house - I'm a simple ice cream man, not a mortgage broker. Though at the rate you're goin', I might need to consider a career change!
<br>
As for yer "culinary catastrophe," I'll have you know it's a best-seller among the discerning palates of, well... those less discerning than yerself, clearly. But since you've been such a ray of sunshine, how about I throw in a free flake? You can use it to write a strongly worded letter to the committee of your choosing.
<br>
Now, will there be anythin' else, or shall I pencil you in for another delightful exchange this time next year?</em><br><br>
<b>Customer</b>: <em>A free flake? Oh, how tremendously generous of you! I'm positively overcome with gratitude. I'll cherish it always, right up until the moment it melts all over my hand in approximately 30 seconds. 
<br>
Look, my good man, I came here for ice cream, not a comedy routine or a lecture on your financial aspirations. If I wanted those, I'd go to a circus or a bank - although at this point, I'm not entirely sure which is which. Now, if you've quite finished with your little performance, I'll take my "best-seller" and be on my way. And don't worry about penciling me in for next year. I'd rather lick the pavement than endure another round of this farcical exchange. Good day to you, sir. I said, good day!</em><br><br>
<b>Shopkeeper</b>: <em>Righto, off you pop then! Mind the step as you dismount from that high horse of yours. And do enjoy yer ice cream - I hear it pairs wonderfully with a side of humble pie!</em><br><br>
