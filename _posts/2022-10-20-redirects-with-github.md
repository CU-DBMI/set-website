---
title: URL redirects with GitHub
author: Vincent Rubinetti
member: vincent-rubinetti
tags:
  - github
---

## Background and motivation

You've likely heard of a service called [Bitly](https://bitly.com/).
It allows you to convert a long link like `some-website.com/a-long-url?search=a-bunch-of-characters` into a shorter one like `bit.ly/98K8eH`.
When someone visits the shorter link, Bitly automatically redirects them to the longer one.
This is helpful when you want to share something frequently and space is limited.

Bitly also offers several other features that you probably want:

- You can customize the text after the `/`, giving you a url that a human could actually remember and type in manually, like `bit.ly/MyCoolLink` (they call these "back-halves").
- You can set up a custom domain to brand your links the way you want, giving you an even nicer and easier-to-remember link, like `my-website.com/MyCoolLink`.
- You can see how many and what kinds of people have used the link over time (i.e. analytics).

This all sounds great, so what's the problem?
Well namely: _Bitly [hides or limits a lot of this functionality behind a paywall](https://bitly.com/pages/pricing)_, and their free plan has become more and more limited over time.
This may not be a problem for you, especially if you value the convenience of having a simple service that handles everything automatically.
And there are certainly [other services that compete with Bitly](https://zapier.com/blog/best-url-shorteners/) which may offer you what you want for free (for now).

But...

## Alternative approach

With just a little bit of setup, we can accomplish all of this in a much better way.
Well, at least much better-suited to the target audience of this article: **People/organizations who use GitHub and Git**.
Hopefully you enjoy working with these tools, or at least have a working knowledge of them.
But if not, don't worry, you can still benefit from this approach!

**The benefits**:

- Free(er)!
  You only need to pay for a domain name, if you want.
- Not subject to the pricing whims of large companies.
  Features and cost won't change.
- Uses tools and workflows you're already accustomed to (and hopefully prefer).
  You don't need to create a new account just for this purpose, like you do with Bitly.
- You get a git history of all of your links; who changed what and when.
- You're in complete control. 
  With a bit of coding knowledge, you can customize it any way you'd like.
  
**The equal**:

- You can customize the text of your links fully, both the domain and "back-halves".
- You can track analytics for your links using whatever service you want, like Google Analytics.
- You can restrict who can see and edit the links using GitHub's private repos and permission settings.
- You can organize your links and add metadata however you like to make maintenance easier.

**The downsides**:

- Significantly more setup.
- Still have to pay for a domain.
- Editing JSON is harder than typing in textboxes.
- More complexity/confusion, if you don't understand the underlying technologies.
- If things go wrong, you have to troubleshoot it yourself (or ask me for help 😉)
