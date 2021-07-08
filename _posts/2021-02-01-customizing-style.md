---
layout: post
title:  Customizing Minima's CSS
date:   2021-02-01 13:03 +0100
---

All themes are customizable. It is also possible to not use a theme at all and start from scratch. 
Here, I decided to continue with Minima's theme for now as there is a lot of documentation available but the idea is the same for all Jekyll themes.

Most of the information needed to start customizing a theme should be available in the theme's README.md in it's repository. However, some details took me some time to understand and get right so this is what is documented here. 

## Stylesheet

#### Choose the right branch on the theme's repository
This site is running on minima v.2.5, the latest stable release: [Minima v.2.5](https://github.com/jekyll/minima/tree/v2.5.1).  
It is important to get the documentation for the right version as the latest (currently v.3.0) version might not work for the oldest ones.

#### Potential error in VSC
Create the stylesheet in `<root>/assets/main.scss`.  
It _must_ start with:  
```  
---  
---  
@import "minima";  
```   
> In Visual Code Studio, this will raise an error: at-rule or selector expected scss (css-ruleorselectorexpected) [1,1].  
> This is because the file start with a dash "-" and can't be removed, but the code will still work.

#### Stylesheet structure
The file's extension is scss just like the rest of minima's styling sheets. On their github, there is a `_saas` folder though. The the main.scss file is written in scss syntax.  
[Read documentation (form sass-lang.com but shows both)](https://sass-lang.com/guide).  
Two things can be customized in this stylesheet:  
- variables which are information that can be reused throughout the stylesheet. They can define fonts, colors or any CSS value. They _must_ be declared **above** the `@import "minima";` line, otherwise it won't work.  
Default variables are found in the `_sass/minima.scss` file.
- any other css (scss) value. Default scss is found in the `_sass/minima` folder.

Any styling done within this stylesheet will override the default theme style.   
Of course styling can be applied to the main content, footer, header, nav-bar etc.
