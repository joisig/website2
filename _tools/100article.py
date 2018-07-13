#!/usr/bin/env python3

import csv
import sys

HEAD = '''<!DOCTYPE html>
<html class="no-js" lang="en-US" prefix="og: http://ogp.me/ns#">
<head>
<meta charset="UTF-8">
<title>100 Startup Tools of the Week</title>
<!--[if lt IE 9]>
<script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script>
<![endif]-->
<meta name="viewport" content="width=device-width; initial-scale=1.0">
<link rel="profile" href="http://gmpg.org/xfn/11" />
<link rel="pingback" href="../xmlrpc.php" />

<!-- This site is optimized with the Yoast SEO plugin v2.3.5 - https://yoast.com/wordpress/plugins/seo/ -->
<meta name="description" content="In honor of our issue #100, here are the 100 tools so far that made it to be tool of the week."/>
<link rel="canonical" href="index.html" />
<meta property="og:locale" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="100 Startup Tools of the Week" />
<meta property="og:description" content="In honor of our issue #100, here are the 100 tools so far that made it to be tool of the week." />
<meta property="og:url" content="index.html" />
<meta property="og:site_name" content="StartupResources.io Blog" />
<meta property="article:section" content="Uncategorized" />
<meta property="article:published_time" content="2018-02-23T09:49:13+00:00" />
<meta property="article:modified_time" content="2018-02-23T09:49:13+00:00" />
<meta property="og:updated_time" content="2018-02-23T09:49:13+00:00" />
<meta property="og:image" content="/images/hunter-haley-424239-unsplash-tools.jpg" />
<meta property="og:image" content="/images/hunter-haley-424239-unsplash-tools.jpg" />
<meta name="twitter:card" content="summary"/>
<meta name="twitter:description" content="In honor of our issue #100, here are the 100 tools so far that made it to be tool of the week."/>
<meta name="twitter:title" content="100 Startup Tools of the Week"/>
<meta name="twitter:site" content="@startupresourcs"/>
<meta name="twitter:domain" content="StartupResources.io Blog"/>
<!-- Begin cookieconsent.insites.com code. -->
<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.css" />
<script src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/3.0.3/cookieconsent.min.js"></script>
<script>
window.addEventListener("load", function(){
window.cookieconsent.initialise({
    "palette": {
      "popup": {
        "background": "#ffffff",
        "text": "#202020"
      },
      "button": {
        "background": "#85D3C9",
        "text": "#ffffff"
      }
    },
    "theme": "classic",
    "position": "bottom-right",
    "content": {
      "message": "This website uses cookies to generate anonymous usage statistics and to analyze audience behavior.",
      "href": "/privacy-policy"
    }
})});
</script>		<!-- End CookieConsent code. -->

<meta name="twitter:image" content="/images/hunter-haley-424239-unsplash-tools.jpg"/>
<meta name="twitter:creator" content="@startupresourcs"/>
<!-- / Yoast SEO plugin. -->

<link rel='dns-prefetch' href='http://fonts.googleapis.com/' />
<link rel='dns-prefetch' href='http://s.w.org/' />
<link rel="alternate" type="application/rss+xml" title="StartupResources.io Blog &raquo; Feed" href="../feed/index.html" />
<link rel="alternate" type="application/rss+xml" title="StartupResources.io Blog &raquo; Comments Feed" href="../comments/feed/index.html" />
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.3\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/2.3\/svg\/","svgExt":".svg","source":{"concatemoji":"http:\/\/startupresources.io\/blog\/wp-includes\/js\/wp-emoji-release.min.js?ver=4.8"}};
			!function(a,b,c){function d(a){var b,c,d,e,f=String.fromCharCode;if(!k||!k.fillText)return!1;switch(k.clearRect(0,0,j.width,j.height),k.textBaseline="top",k.font="600 32px Arial",a){case"flag":return k.fillText(f(55356,56826,55356,56819),0,0),b=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,56826,8203,55356,56819),0,0),c=j.toDataURL(),b===c&&(k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447),0,0),b=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447),0,0),c=j.toDataURL(),b!==c);case"emoji4":return k.fillText(f(55358,56794,8205,9794,65039),0,0),d=j.toDataURL(),k.clearRect(0,0,j.width,j.height),k.fillText(f(55358,56794,8203,9794,65039),0,0),e=j.toDataURL(),d!==e}return!1}function e(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var f,g,h,i,j=b.createElement("canvas"),k=j.getContext&&j.getContext("2d");for(i=Array("flag","emoji4"),c.supports={everything:!0,everythingExceptFlag:!0},h=0;h<i.length;h++)c.supports[i[h]]=d(i[h]),c.supports.everything=c.supports.everything&&c.supports[i[h]],"flag"!==i[h]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[i[h]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(g=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",g,!1),a.addEventListener("load",g,!1)):(a.attachEvent("onload",g),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),f=c.source||{},f.concatemoji?e(f.concatemoji):f.wpemoji&&f.twemoji&&(e(f.twemoji),e(f.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel='stylesheet' id='mh-google-fonts-css'  href='http://fonts.googleapis.com/css?family=Lato:300italic,300,400italic,400,900|Vollkorn:400,400italic' type='text/css' media='all' />
<link rel='stylesheet' id='mh-font-awesome-css'  href='../wp-content/themes/mh-purity-lite/includes/font-awesome.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='mh-style-css'  href='../wp-content/themes/mh-purity-lite/style6d3d.css?ver=v1.0.7' type='text/css' media='all' />
<script type='text/javascript' src='../wp-includes/js/jquery/jqueryb8ff.js?ver=1.12.4'></script>
<script type='text/javascript' src='../wp-includes/js/jquery/jquery-migrate.min330a.js?ver=1.4.1'></script>
<script type='text/javascript' src='../wp-content/themes/mh-purity-lite/js/scriptsef15.js?ver=4.8'></script>
<link rel='https://api.w.org/' href='../wp-json/index.html' />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="../xmlrpc0db0.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="../wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 4.8" />
<link rel='shortlink' href='../indexe856.html?p=121' />
<script data-cfasync="false" src="//load.sumome.com/" data-sumo-site-id="51d0b0727005b9932a68b8c308124ed7da448fb9c54bc54a5d4b1af10633183d" async></script>
<!--BEGIN: TRACKING CODE MANAGER BY INTELLYWP.COM IN HEAD//-->
<!-- start ConvertFox JS code ---
<script>
(function(d,h,w){var convertfox=w.convertfox=w.convertfox||[];convertfox.methods=['trackPageView','identify','track','setAppId'];convertfox.factory=function(t){return function(){var e=Array.prototype.slice.call(arguments);e.unshift(t);convertfox.push(e);return convertfox;}};for(var i=0;i<convertfox.methods.length;i++){var c=convertfox.methods[i];convertfox[c]=convertfox.factory(c)}s=d.createElement('script'),s.src="//d3sjgucddk68ji.cloudfront.net/convertfox.min.js",s.async=!0,e=d.getElementsByTagName(h)[0],e.appendChild(s),s.addEventListener('load',function(e){},!1),convertfox.setAppId("aznv6k3t"),convertfox.trackPageView()})(document,'head',window);
</script>
___ end ConvertFox JS code-->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','http://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-101988152-1', 'auto');
  ga('send', 'pageview');

</script>
<!--END: https://wordpress.org/plugins/tracking-code-manager IN HEAD//--><link rel="icon" href="../wp-content/uploads/2015/11/cropped-twitter-startupresourcesio-32x32.jpg" sizes="32x32" />
<link rel="icon" href="../wp-content/uploads/2015/11/cropped-twitter-startupresourcesio-192x192.jpg" sizes="192x192" />
<link rel="apple-touch-icon-precomposed" href="../wp-content/uploads/2015/11/cropped-twitter-startupresourcesio-180x180.jpg" />
<meta name="msapplication-TileImage" content="http://startupresources.io/blog/wp-content/uploads/2015/11/cropped-twitter-startupresourcesio-270x270.jpg" />
</head>
<body class="post-template-default single single-post postid-121 single-format-standard">
<div class="container">
<header class="header-wrap">
	<a href="../index.html" title="StartupResources.io Blog" rel="home">
<div class="logo-wrap" role="banner">
<img class="header-image" src="../wp-content/uploads/2015/11/cropped-bloglogo1.jpg" height="191" width="373" alt="StartupResources.io Blog" />
<div class="logo logo-overlay">
<h1 class="logo-name">StartupResources.io Blog</h1>
<h2 class="logo-desc">Resources &amp; Writings</h2>
</div>
</div>
</a>
	<nav class="main-nav clearfix">
		<div class="menu"></div>
	</nav>
</header><div class="wrapper clearfix">
	<div class="content left"><article class="post-121 post type-post status-publish format-standard hentry category-uncategorized">
	<header class="post-header">
		<h1 class="entry-title">100 Startup Tools of the Week</h1>
		<p class="meta post-meta clearfix">
			<span class="updated meta-date"><i class="fa fa-calendar"></i>February 23, 2018</span>
			<span class="vcard author meta-author"><span class="fn"><i class="fa fa-user"></i>Jói</span></span>
			<span class="meta-tags"><i class="fa fa-tag"></i><a href="../uncategorized/index.html" rel="category tag">Uncategorized</a></span>
			<span class="meta-comments"><i class="fa fa-comment-o"></i>0</span>
		</p>
	</header>
	<div class="entry clearfix">

<div class="post-thumbnail">
<img src="/images/hunter-haley-424239-unsplash-tools.jpg" alt="" title="tools" />
</div>

<h1>100 Startup Tools of the Week</h1>
<p>
Today marks issue #100 of the Startup Resources newsletter, and it seemed like a
good idea to do something in the theme of 100. Behold, this blog post! For most
of those 100 newsletters we’ve had a tool of the week selected (and for those
few where we didn’t, I chose my favorite of the mentioned tools from that
newsletter). Here is the list of all 100 super-useful tools of the week, in the
same order they were featured in the newsletters. Enjoy!
</p>
<p>&nbsp;</p>
'''

FOOT = '''</div>
	</article>

	</div>
	<aside class="sidebar sb-right">
	<div class="sb-widget"><form role="search" method="get" id="searchform" action="http://startupresources.io/blog/">
    <fieldset>
	<input type="text" value="" name="s" id="s" />
	<input type="submit" id="searchsubmit" value="Search" />
    </fieldset>
</form></div><div class="sb-widget"><h4 class="widget-title">About StartupResources.io</h4>			<div class="textwidget"><p>Looking for the best tools and solutions for your Startup? <a href="../../index.html">Check out StartupResources.io</a> for categorized lists of the best tools, with categories like A/B Testing, Social Media tools, Growth Hacking, Pre-Launch Traction, and Espionage.</p>
<br>
<hr>
<br>
<p>Interested in guest posting here? Have a case study or an article to share? <a href="mailto:info@startupresources.io">email me</a> and tell me your ideas.</p></div>
		</div>		<div class="sb-widget">		<h4 class="widget-title">Recent Posts</h4>		<ul>
			<li>
				<a href="/blog/the-tools-your-startup-should-be-using-and-why/">The Tools Your Startup Should be Using and Why</a>
			</li>
			<li>
				<a href="/blog/gdpr-the-quick-and-dirty-guide-to-getting-compliant-for-startups-and-small-business/">GDPR: The Quick and Dirty Guide to Getting Compliant for Startups and Small Business</a>
			</li>
			<li>
				<a href="/blog/100-startup-tools-of-the-week/">100 Startup Tools of the Week</a>
			</li>
			<li>
				<a href="/blog/how-to-pitch/">Pitching your startup: Lessons learned</a>
			</li>
			<li>
				<a href="/blog/the-zero-subscription-startup-stack-part-two/">The $0 Subscription Startup Stack 2/4: Start selling</a>
			</li>
			<li>
				<a href="/blog/the-zero-subscription-startup-stack-part-one/">The $0 Subscription Startup Stack 1/4: Build something and run it</a>
			</li>
					<li>
				<a href="index.html">9 Tactical Tips on how to be #1 on Product Hunt all day</a>
						</li>
					<li>
				<a href="../how-to-use-twitter-to-butter-up-influencers-so-that-they-will-let-you-guest-blog/index.html">How To Use Twitter To Butter Up Influencers So That They Will Let You Guest Blog</a>
						</li>
					<li>
				<a href="../user-surveying-to-find-and-fix-conversion-issues/index.html">User surveying to find and fix conversion issues</a>
						</li>
					<li>
				<a href="../researching-customer-fears/index.html">Researching Customer Fears</a>
						</li>
					<li>
				<a href="../why-you-need-customer-discovery/index.html">Why You Need Customer Discovery</a>
						</li>
				</ul>
		</div>		</aside></div>
<div class="copyright-wrap">
	<p class="copyright">Copyright &copy; 2018 | <a href="http://www.mhthemes.com/" rel="nofollow">MH Purity <em>lite</em> WordPress Theme by MH Themes</a> | <a href="/privacy-policy" style="text-decoration: none;">Privacy Policy</a> | <a href="/data-protection" style="text-decoration: none;">Data Protection</a><br/><a href="https://www.paved.com/sites/startupresources-io?ref=joisigurdsson2" style="text-decoration: none;">Want to sponsor our newsletter?</a></div>
</div>

<!--BEGIN: TRACKING CODE MANAGER BY INTELLYWP.COM IN FOOTER//-->
<!-- BEGIN PRIVY WIDGET CODE -->
<script type='text/javascript'> var _d_site = _d_site || '4F843DF71A2DB1EEC91F14C1'; </script>
<script src='//widget.privy.com/assets/widget.js'></script>
<!-- END PRIVY WIDGET CODE -->
<!--END: https://wordpress.org/plugins/tracking-code-manager IN FOOTER//--><script type='text/javascript' src='../wp-includes/js/wp-embed.minef15.js?ver=4.8'></script>
</body>
</html>
'''

items = []
categories = {}

with open(sys.argv[1], 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        (num, full, category, name, url, alive, description) = row
        items.append([num, category, name, url, description])
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

items = items[1:]

print(HEAD)
for item in items:
    (num, category, name, url, description) = item
    print("<div style='display: inline-block'>")
    print("<img class='alignleft' src='http://img.bitpixels.com/getthumbnail?code=6929743343830560&size=120&url=" + url + "'>")
    print("#" + num + ": <a href='" + url + "' target='_blank'>" + name + "</a>: " + description)
    print("</div>")
    print("<p>&nbsp;</p>")
print(FOOT)

print(categories, file=sys.stderr)
