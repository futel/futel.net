---
layout: post
title: Futel Unauthorized FAQ - by breedx
---

Hey you old so and so... look at you, reading a physical zine printed on actual paper. I'm breedx, nice to meet you. I've had the pleasure of helping out with the Futel project for a few turns of the rotary dial now. Sometimes I'm just hacking up some poorly written usage code, and other times I'm digging trenches in the field or grinding a phone open at the physical plant. Phew! Helping out with Futel sure is hard work... but it's super educational and rewarding too!

I enjoy this project immensely... so much so that I will talk about it to basically anyone who will listen. One thing I've noticed is that people who learn about the project tend to ask the same questions time after time. Because of this, I thought it might be helpful to put together a little unofficial (OK, fine, "unauthorized" sounds way cooler) list of frequently asked questions, along with my best attempt at answering them.

**Q:** Can I get a phone?

**A:** Probably, thanks for the interest! We are always looking for awesome new      public locations, especially in underserved areas or where coverage is      lacking. Honestly, it's a commitment that I think most folks just plain      forget about or lose interest in after the initial excitement wears off. If      we can fund it, and you are serious, we will try and work with you.

**Q:** How do you pay for all this?

**A:** In short, the project is funded almost entirely through grants with help      from contributors. As far as I know, Karl does all the grant writing and      paperwork/logistics around that. Russel and Personal Telco Project (our      fiscal sponsor) help keep the nonprofit stuff in order. Check out the page      at https://futel.net/support/ for a list of past and current sponsors. The      support page also links to ways that you can help fund Futel, with cash via      Patreon or by purchasing shirts, buttons, and zines (like this one!). I bet      you have a friend who wants one <hint hint>.
  
**Q:** How many phones have y'all installed?

**A:** Honestly, it changes often enough that I usually can't give an accurate      answer, so I just resort to cheating by looking at the map      (https://futel.net/map/). Unfortunately, the map is also updated somewhat      infrequently, but it's likely within one or two phones. Right now it looks      like we have 19 installed phones!

**Q:** Does 911 work?

**A:** Yes, it's actually truly 100% legit 911 that knows the phone location, so      use ONLY in case of an emergency please.

**Q:** Don't people mess with them or steal them?

**A:** Well, we want people to mess with them, so yeah, but please don't break the      phones (they're getting harder to come by each year!). The most common      problem I've seen is the broken handset, but all manner of abuse and smashy      smash happens from time to time. As the network grows, so does the      maintenance burden, which is unfortunate... but also keeps us busy.

**Q:** Aren't these just being ab/used for drug deals?

**A:** Um, this ain't the 1980s, so not really, no. Sure, it's in the realm of      possibility, but even if it was happening I don't think we'd have any way      of confirming or refuting that. I also think that people today who need      anonymous and/or ephemeral communications just use snapchat or whatsapp      without being tied to a fixed geo location.

**Q:** What do you know about the Willamette Valley Dre<scrrreeeeeeeaaaach>

**A:** Get the fuck out of here with that.

**Q:** What's the tech stack like?

**A:** Oh it's cool yeah thanks for asking. The short answer is: It's complicated.      The longer answer is: It's not that complicated. The setup at a physical      location is fairly straightforward: A phone is connected via RJ11 cable      back to a little device called an Analog Telephone Adapter (ATA), which      allows the phone to operate over the host's internet. Folks will also refer      to the ATA colloquially as a "sip box". Anyway, Karl knows all this stuff      better than most of us, but each ATA is preconfigured to connect to the      "futel network" as a specific extension. Originally, all behavior was      controlled by custom programming for the Asterisk open source PBX system,      but nowadays almost everything is programmed in Twilio Programmable Voice.      Most of the phones have menus that behave similarly (like pressing 1 to      make a call), but not all phones (extensions) are programmed the same. For      example, the utilities and services offered in one city will be different      than the services in another city. The incoming line is also not the same.      We really try and be as transparent as possible with all of the code, so      everything (code, docs, website, everything) is hosted in public GitHub      (https://github.com/futel) for you to enjoy.

**Q:** Do you record the audio of the calls?

**A:** No way. Why would you even suspect that? Ugh. Yuck. It would probably be illegal,     but who cares... we respect our users right to privacy -- so no, voice calls on the Futel       network are not recorded. Voicemails left for the operator are recorded. :-)

  Well, that's all the time we have for now. If you have other questions that   haven't been answered here, you can always direct them to a friendly Futel   operator by dialing zero (0) from any Futel telephone.
