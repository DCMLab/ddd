---
layout: post
title:  "How to change theme"
date:   2021-02-01 10:41 +0100
category: customizing jekyll
---

This is how to change theme on a Jekyll/Github static website. 

1. Find a theme to use, for example on [rubygems](https://rubygems.org/search?query=jekyll+theme).
2. Install the new theme:
    * Change the theme in the `_config.yml` file: ```theme: <THEME-NAME>```.
    > Find more theme specific informations on the theme's github repository.
    * Add the gem to the project's Gemfile: ```gem "<THEME-NAME>```
    * Run `bundle install` in the terminal.
3. Correct the front matter of existing pages and posts if necessary. 
    * The layout _must_ refer to one of the theme's available layout (found in the _layout folder the theme's github)

That's it!
