---
title: URL redirects with GitHub
author: Vincent Rubinetti
member: vincent-rubinetti
tags:
  - github
---

⤵️ **[Skip to the setup](#setup)** ⤵️
{:.center}

## Background and motivation

You've likely heard of a service called [Bitly](https://bitly.com/).
It allows you to convert a long link like `some-website.com/a-long-url?search=a-bunch-of-characters` into a shorter one like `bit.ly/98K8eH`.
When someone visits the shorter link, Bitly automatically "redirects" them to the longer one.
This is helpful when you want to share something frequently and space is limited.
You can think of it like a shortcut.

Bitly also offers several other features that you probably want:

- You can customize the text after the `/`, giving you a url that a human could actually remember and type in manually, like `bit.ly/MyCoolLink` (they call these "back-halves").
- You can set up a custom domain to brand your links the way you want, giving you an even nicer and easier-to-use link, like `my-website.com/MyCoolLink`.
- You can see how many and what kinds of people have used the link over time (i.e. analytics).

This all sounds great, so what's the problem?
Well namely: _Bitly [hides or limits a lot of this functionality behind a paywall](https://bitly.com/pages/pricing)_, and their free plan has become more and more limited over time.
This may not be a problem for you, especially if you value the convenience of having a simple service that handles everything automatically.
And there are certainly [other services that compete with Bitly](https://zapier.com/blog/best-url-shorteners/) which may offer you what you want for free (for now).

But...

{% include section.html %}

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
  You can use GitHub's private repos and permission settings to control who can see and edit your links.
- You get a nice git history of all of your links; who changed what and when.
- You're in complete control.
  With a bit of coding knowledge, you can customize it any way you'd like.
  Notably, you can use whatever analytics service you want, like Google Analytics.

**The equivalent**:

- You can customize the text of your links fully, both the domain and the part after the `/`.
- You can track analytics for your links.
- You can restrict who can see and edit the links.
- You can organize your links and add metadata however you like to make maintenance easier.

**The downsides**:

- Significantly more setup.
- Still have to pay for a domain.
- The target links are not truly 100% hidden from the public.
  See footnote about obfuscation.
- Editing JSON is harder than typing in textboxes, and you could accidentally break the formatting.
- More complexity/confusion, if you don't understand the underlying technologies.
- If things go wrong, you have to troubleshoot it yourself (or ask me for help 😉)

{% include section.html %}

## How it works

{%
  include figure.html
  image="images/redirects-diagram.jpg"
  caption="Diagram of the basic components of this redirects approach."
  width="420px"
%}

You have a private _redirects_ GitHub repository that contains your redirects data (where you want to redirect from and to) in [`.json`](https://en.wikipedia.org/wiki/JSON) files.
Only people you choose can see or edit this data.
You also have a public _website_ GitHub repository that hosts a barebones webpage that actually performs the redirecting when a user visits a link.
You can set this website up at a custom domain to make your links shorter and nicer.

Adding/removing/changing a link goes like this:

1. You makes a change to one of the `.json` files in the _redirects_ repo.
2. `deploy.yaml` tells [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) that any time someone commits a change to the repo, it should automatically run the `encode.js` script.
3. The `encode.js` script combines and encodes your `.json` file data into a form that isn't searchable or human-readable[^1].
4. `deploy.yaml` then tells GitHub to take the result of the `encode.js` script, and commit it to the `redirect.js` script in the _website_ repo.
5. [GitHub Pages](https://pages.github.com/) detects a change in the `redirect.js` script, and updates the website.

Then, a user visiting a link goes like this:

1. They navigate to a link, e.g. `/chatroom`.
2. `chatroom.html` isn't a page on the website, so GitHub loads `404.html` for the user instead (but preserves the `/chatroom` url), which runs some scripts.
3. The `analytics.js` script immediately runs, which sends[^2] data like page, IP, location, etc. off to Google Analytics or whoever.
4. The `redirect.js` script decodes the redirect data previously encoded from the _redirects_ repo, finds the url in the redirect data, and immediately navigates there instead.

So let's figure out how to make this work!

{% include section.html %}

## Setup

{% include section.html %}

[^1]: This does not _encrypt_ your redirect data, it only _obfuscates_ it. Anyone with some coding knowledge – or maybe someone who read this article – could still figure out your redirect data with some effort. The way this method works, true encryption is impossible because any key needed for decryption would also need to be in the `redirect.js`, which the attacker would have access to.
[^2]: The analytics service you're using _should_ be able to capture all the necessary data in time, before the redirection happens. But these services' scripts are usually closed source, so we can't know for sure exactly how they work. However, in testing with Google Analytics at least, everything seems to be captured fine.
