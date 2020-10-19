import pdfplumber
from gtts import gTTS

# article source: https: // www.wired.com/story/what-forest-floor-playgrounds-teach-us-about-kids-and-germs/
article = """
AS DUSK FELL on the Finnish city of Lahti on a still chilly day in May 2016, a crew of workers let themselves into the yard of an empty daycare center. Underneath the swings and jungle gyms, they installed squares of forest floor—scruffy shrubs, shin-high berry bushes, wispy meadow grasses, and velvety mounds of moss—harvested from the woods somewhere in a less developed part of the country. Around the edges, they put in soft green sod. In the morning, when the children arrived, they found their playground—formerly a drab patchwork of asphalt, gravel, and sand—transformed overnight into micro-oases of wilderness.

This scenario played out three more times that month at daycares in Lahti, and 500 miles to the west, in the city of Tampere. It wasn’t the work of some nature-loving guerrilla artists, but the start of an ambitious science experiment to find out if the lack of microbes in paved-over urban environments could be turning people’s immune systems against them. “There is this ‘biodiversity hypothesis,’ that in the absence of diverse environmental microbiota, people are more likely to get immune-mediated diseases,” says Aki Sinkkonen, an evolutionary ecologist at the Natural Resources Institute Finland. “But no one had really tested this with children.”

You’re probably more familiar with the “hygiene hypothesis.” First described by a British epidemiologist named David Strachan in the early 1990s, it posits that the rise in chronic disorders related to overreactive immune systems—such as asthma, diabetes, and allergies—is driven by children growing up in increasingly sterile bubbles. Immune systems are, at their most basic, object classifiers. Their job is to recognize what’s self and what’s other. Microbes encountered early in life are the first tutors in this process—helping the developing immune system decipher what’s dangerous and what is not. The more families have used antibacterial soaps and gels, sealed themselves into high-rise apartments, and driven cars through concrete jungles, the less habitat there has been for bacteria, protozoa, fungi, and viruses to thrive—and the less likely it’s been for kids’ developing immune systems to run into them. And less exposure has meant fewer opportunities to train. A poorly trained immune system could fail when it comes time to distinguish between a body’s own cells and food allergens, or gut microbes, or pollen in the air.

Lab experiments on rodents in the early 2000s supported this idea: Wild rats had immune systems well-tuned to fight dangerous pathogens, but not minor irritants, whereas their lab-raised counterparts went into overdrive at the smallest stimulus. Human epidemiological studies lent circumstantial evidence too—allergy and asthma rates tend to be higher in more industrialized areas than in rural ones. To counteract these supposed negative effects of urban, modern lifestyles, dozens of companies have sprung up to hawk immune-boosting probiotics—pills and drinks and creams filled with cocktails of live bacterial cultures. In the Covid-19 era, thousands of posts tagged #immuneboost promoting these and other home remedies show up on Instagram each week. So far, there’s little evidence any of it has worked.

Which is why, in recent years, scientists like Sinkkonen have taken this idea one step further. People are increasingly living in microbiodiversity deserts, they observed, missing out on exposure to a variety of harmless bugs. “The immune system doesn’t recognize microbes by species, but by their type,” says Sinkkonen. “Probiotics usually contain only one or two types of bacteria, so it’s unlikely to activate the whole immune system. We wanted to see what would happen if we brought in a whole diverse microbial environment.” Hence, the forest floors in the playgrounds—the first randomized controlled trial to test the biodiversity hypothesis in kids. Biohacking, but make it cute.

Sinkkonen’s team recruited 75 kids ages 3 to 5, all of whom attended one of seven daycares with similarly depressing postage-stamp playgrounds, and all of whom reported having similar numbers of siblings, pets, time spent outdoors, and fruits and vegetables consumed. (The goal here was to minimize any potential confounding variables.) To further ensure uniformity, for one month, all the kids were served three uniform meals daily—breakfast, lunch, and afternoon snack. Prior to the intervention, a nurse swabbed the childrens’ forearms and took blood samples, a way of tracking the proteins and other signaling molecules that provide a picture of how an immune system is functioning.

Four of these daycares received the overnight greening treatment, and three—the negative controls—did not. Compared to an urban sandbox, each gram of the newly laid forest-supporting soil contained roughly 500 times as many microbes. For four weeks, all of the kids played outside for an average of 90 minutes each day. The only difference was some kids got to run and root around in the renovated yards, and some of them were still playing atop asphalt and gravel. (There was also a positive control group of demographically and behaviorally matched kids who attended daycare at nature centers located in the actual woods.)

At the end of four weeks, the kids’ arms were swabbed and their blood was drawn again, and Sinkkonen’s team began analyzing the results. In a study published Wednesday in Science Advances, they found that the children who had been playing in the newly forested spaces had more diverse communities of friendly bacteria living on their skin. Specifically, alphaproteobacteria species seemed to flourish. Not surprising: Previous studies have shown this subgenre to be associated more often with children who grow up on farms than city kids.

The blood tests showed that kids who had played on the imported forest floor had also developed a higher ratio of inflammation-dampening molecules to pro-inflammatory ones. Levels of interleukin-10—a cytokine that prevents damage to a host’s tissues during injury or infection—went up while levels of interleukin-17A went down. IL-17 is secreted by a group of T cells whose job it is to recruit other kinds of immune cells to fight off invading pathogens. Sinkkonen says this is a signal that the kids’ immune systems were engaging with all the new bugs they were encountering. The skin and blood samples from the forest playground group looked much more like the positive control group, who played at daycares in the woods.

These results suggest it might be possible to dial childrens’ immune systems to a well-balanced state simply by greening up the environments around them, says Sinkkonen. “I was quite surprised to see such highly significant changes to occur in such a short amount of time,” he says. It implies that the immune system is still extremely pliable at that young age. Over time, it becomes more stubbornly set in its ways. “I think that every child should have access to this kind of environment. They have more to win and more to lose,” he continues.

The results are in line with early data from several large studies run out of the lab of Jack Gilbert, a microbiologist at the University of California, San Diego, and cofounder of the Earth Microbiome Project. His group has been working for the past 10 years to map the unique microbial communities that live in houses, offices, and hospitals, and study what happens to the health of the occupants when new bugs are introduced. Gilbert says studies like the Finnish playground trial are something he’s wanted to do for a while, but because of cost and practicality, he’s been running much more limited experiments—indoors, and with just a few isolated bacterial species. “This is very cool!” he wrote in an email to WIRED.

Gilbert cautions that both the sample size and effects on the kids were small, so one shouldn’t read too much into these results, but he feels they are a good first step. “I am really excited to see this study replicated at a larger level, and ideally with long-term follow-up to examine the influence on chronic immune health outcomes,” he wrote.

Sinkkonen’s team did follow the playground cohort for two years, to see if the kids that played in the green spaces had lower rates—or less severe forms—of allergies, asthma, and other immune-mediated diseases. Those results have yet to be published, but Sinkkonen says the trial was likely too small to pick up any long-term effects, if they do exist. That’s why his group is currently recruiting infants for a much larger trial, for which the plan is to give new parents special swaddling sheets lined with microbe-powder-filled pockets. They’ll monitor those babies as they grow up and compare them to children who were wrapped in more sterile materials, to see if the early microbial exposure changes the trajectory of their immune development, and if it can actually alter the course of developing diseases related to immune overreactivity. “This is the next major step,” says Sinkkonen.

For now though, he’s busy helping get more green spaces into playgrounds. As a result of his study, the municipal governments of Lahti and Tampere have allocated funding to get forest floors and other natural elements like vegetable gardens into places where kids will regularly use them. Sinkkonen’s team is advising them on the kinds of soils to bring in and the landscaping designs that are most likely to engage kids. The Finnish Ministry of Education and Culture also set aside grant money that cities can apply for to launch their own projects.

As for the children in the initial study? The researchers’ plan was to remove the greenery at the conclusion of the experiment. But the kids loved it so much that Sinkkonen’s team decided not to. Some of those children have since graduated to grade school. But the forest floors are still out there, still growing among the asphalt, still getting kids good and dirty.
"""

####### ARTICLE
language = 'en'
 gtts_transformer = gTTS(text=article, lang=language)
 gtts_transformer.save("wired_article.mp3")
 print("WORK DONE")

###### PDF
#pdf_path = "book.pdf"
#
#pdf = pdfplumber.open(pdf_path)
#page = pdf.pages[150]
#text = page.extract_text()
#print(text)
#pdf.close()
#
#language = 'en'
#gtts_transformer = gTTS(text=text, lang=language)
#gtts_transformer.save("audiobook.mp3")
#print("WORK DONE")
