remove_attribute = {'https://angelnumber.org': {'id': ['M381992ScriptRootC303780'],'class': ['hm-related-posts','cat-links']},
                    'https://angelmanifest.com': {'class': ['wp-block-embed is-type-wp-embed is-provider-angel-manifest wp-block-embed-angel-manifest','entry-meta','ct-breadcrumbs']},
                    'https://www.angelsnumbers.com/':{'id': ['le_body_row_8'], 'class': ['op-custom-html-block','breadcrumb-style-7']},
                    'https://www.coolastro.com/':{'id': ['comments','ez-toc-container'], 'class': ['entry-meta','relpost-thumb-wrapper']},
                    'https://divineangelnumbers.com/':{'id':['comments', 'grow-me-in-content-recs-root'],'class': ['uagb-toc__wrap', 'entry-category-icon', 'entry-meta clear', 'social-share-icons', 'has-background','author-box clear', 'entry-related clear', 'wp-block-image']},
                    'https://www.guardian-angel-reading.com/': {'id': ['share'],'class': ['related-articles fixedfont','homeform homeform--og ', 'byline author vcard']},
                    'https://hiddennumerology.com/': {'id': ['ez-toc-container', 'dpsp-content-bottom', 'grow-me-in-content-recs-root'], 'class':['purplebox','pinkbox','yellowbox', 'emalsubinpt', 'saboxplugin-tab', 'dpsp-share-text ', 'navigation post-navigation']},
                    'https://www.adviseastro.com' : {'id':['ez-toc-container'],'class':['entry-meta']},
                    'https://www.ipublishing.co.in/' : {'id':['toc_container'],'class':['entry-meta']},
                    'https://joynumber.com/' : {'id':['toc_container'],'class':['css-ujfvsi eods1cv1','css-v5rwlu eods1cv8','css-nq5slz e16ntblo5','css-75up63 e1nq2w9512', 'css-19p6q85 ecyq0i81']}, #problem in 777
                    'https://mattbeech.com/' : {'id':['toc_container', 'single-comments'],'class':['breadcrumb']},  #need replace_code
                    'https://www.mindbodygreen.com/' : {'class':['subcategory-label c-dark-purple ', 'editor-info__text', 'article-subnavigation', 'ad__callout container', 'article-header__share-like article-header__share-like--standard  article-header__share-like--p2', 'article-image article-image--p1 article-image--hero article-image--hero-standard ', 'article-affiliate-disclaimer', 'article-date article-date--standard', 'article-header__share-like-wrapper', 'article-header__share-like-wrapper article-header__share-like-wrapper--alt']},
                    'https://www.mindfulnessandjustice.org/' : {'class':['saboxplugin-wrap', 'entry-meta', 'InlineRecs___StyledDiv3-sc-7gga64-8 kMYAEH', 'code-block code-block-1']},
                    'https://trustedpsychicmediums.com':{'class':['entry-meta','irp','entry-author author-bottom','tag-cloud','entry-related-posts'],'itemprop':['articleSection'],'id':['toc_container','respond','entry-actions','entry-related-posts']}, #24
                    'https://numerologycolumn.com/' : {'id':['toc_container'],'class':['code-block code-block-1','author-card', 'recent-articles-container', 'entry-meta sr-only'],'href':["https://numerologist.com/anf-mesl/denpet"]}, #17
                    'https://numerologynation.com/' : {'id':['toc_container'],'class':['ck_form', 'entry-meta', 'rank-math-breadcrumb']},
                    'https://numerologysign.com/' : {'id':['mv-trellis-comments'],'class':['article-meta post-meta-wrapper post-meta-single post-meta-single-top', 'su-button-center', 'ShadowDomContainer___StyledDiv-paiu0k-0', 'entry-footer', 'navigation post-navigation']},
                    'https://www.psychnewsdaily.com/' : {'class':['author-box ct-hidden-sm', 'simpletoc-title', 'adthrive-player-title']},
                    'https://www.ryanhart.org/' : {'class':['post-comments', 'center w-100 br3 hidden ba b--grey-3 mv4', 'mw7 center', 'mw7 mv4 center sans-serif tc', 'f7 grey-3 sans-serif', 'f7 flex justify-between grey-3 sans-serif']},
                    'http://sacredscribesangelnumbers.blogspot.com' : {'class':['post-footer', 'MsoNormal'], 'href': ['https://www.etsy.com/au/shop/JoWPottery','http://numerology-thenumbersandtheirmeanings.blogspot.com/', 'http://www.facebook.com/JoWPottery/', 'http://sacredscribes.blogspot.com.au/p/about-joanne-sacred-scribes.html', 'http://sacredscribes.blogspot.com.au/2016/10/joanne-sacred-scribes-websites-blogs.html']},
                    'https://numeroscop.net/': {'class':['header', 'n-square', 'angel-realted-posts']},
                    'https://researchmaniacs.com/': {'id': ['177976545'],'class':['header', 'n-square', 'angel-realted-posts']},
                    'https://www.sunsigns.org/': {'id':[''], 'class': ['single-post-video', 'post-meta', 'share-post']}
                    }

page_xpath = [('https://hiddennumerology.com',"//main[@id='main']"),  #10
              ('https://www.adviseastro.com',"//div[@class='inside-article']"),  #1
              ('https://angelmanifest.com',"//div[@class='hero-section']|//div[@class='entry-content']"),  #2
              ('https://angelnumber.org/', '//*[@id="main"]'),  #4
              ('https://angelnumbersmeaning.com//', '//*[@id="main"]'),  #5
              ('https://www.angelsnumbers.com/', '//*[@id="content_area"]'),  #6
              ('https://www.coolastro.com/','//*[@id="primary"]'),  #7
              ('https://divineangelnumbers.com/','//*[@id="main"]'),  #8
              ('https://www.guardian-angel-reading.com/','//*[@id="sticky-anchor"]/div/main'),
              ('https://angelnumber.me','//div[@class="ast-post-format- single-layout-1 ast-no-date-box"]'),  #3
              ('https://www.ipublishing.co.in/','//*[@class="inside-article"]'),  #11
              ('https://joynumber.com/', '//*[@id="gatsby-focus-wrapper"]/div[2]/div[1]'), # 12
              ("https://mattbeech.com/",'//*[@class="container"]'), #13
              ("https://www.mindbodygreen.com/",'//*[@class="main-content__article-body"]'), #14
              ("https://www.mindfulnessandjustice.org/",'//*[@id="main"]'), #15
              ('https://trustedpsychicmediums.com',"//main[@id= 'main']"),
              ('https://www.mindyourbodysoul.com',"//main[@id='content']"),
              ('https://numerologycolumn.com/',"//main[@id= 'main']"), #25
              ('https://numerologynation.com/',"//div[@class= 'inside-article']"), #17
              ('https://numerologysign.com/',"//*[@id='content']"), #18
              ('https://www.psychnewsdaily.com/','//*[@id="main"]'), #19
              ('https://www.ryanhart.org/','//*[@class="fl mw6 ph2 pv2 cms"]'),
              ('http://sacredscribesangelnumbers.blogspot.com','//*[@class="post hentry uncustomized-post-template"]'),
              ('https://numeroscop.net/','//div[@class= "container body"]'),
              ('https://researchmaniacs.com/','//div[@class= "title" ] | //div[@class= "content"]'),
              ('https://www.sunsigns.org/','//*[@id="the-post"]')
              ]
ignore_tag_by_domain = {'https://angelmanifest.com': ['ul'],
                        'https://www.psychnewsdaily.com': ['ul'],
                        'https://numeroscop.net': ['nav', 'aside'],
                        'https://researchmaniacs.com': ['font'],
                        'https://www.sunsigns.org': ['ul', 'center', 'form']}
page_wise_delimeter = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
para_wise_delim = '@@@@@@@@@@@@@@@@@@@'
ignore_site_num = [1,2,3,4,5,6,7,8,9,10,11,13,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
url_patterns = {'1':  ["https://www.adviseastro.com/angel-number-@#$-meaning-and-symbolism/"],
        '2':  ['https://angelmanifest.com/angel-number-@#$/'],
        '3':  ["https://angelnumber.me/@#$-meaning/"],    #no remove attribute need to add for this page
        '4':  ["https://angelnumber.org/@#$-angel-number/","https://angelnumber.org/@#$-angel-number-meaning-and-symbolism/"],
        '5':  ["https://angelnumbersmeaning.com/@#$-angel-number/","https://angelnumbersmeaning.com/angel-number-@#$-meaning-and-symbolism/","https://angelnumbersmeaning.com/angel-number-@#$/"],
        '6':  ["https://www.angelsnumbers.com/meaning/number-@#$/"],
        '7':  ["https://www.coolastro.com/angel-number-@#$-meaning-and-symbolism/"],
        '8':  ["https://divineangelnumbers.com/@#$-angel-number-meaning","https://divineangelnumbers.com/angel-number-@#$-meaning","https://divineangelnumbers.com/angel-number-@#$-meaning","https://divineangelnumbers.com/angel-number-@#$","https://divineangelnumbers.com/@#$-angel-number"],
        '9':  ["https://www.guardian-angel-reading.com/blog-of-the-angels/@#$-angel-number/","https://www.guardian-angel-reading.com/blog-of-the-angels/angel-number-@#$/","https://www.guardian-angel-reading.com/blog-of-the-angels/@#$-angel-number-meaning/"],
        '10': ["https://hiddennumerology.com/angel-number-@#$/"],
        '11': ["https://www.ipublishing.co.in/angel-number-@#$-meaning","https://www.ipublishing.co.in/angel-number-@#$"],
        '12': ["https://joynumber.com/@#$-angel-number/","https://joynumber.com/angel-number-@#$/","https://joynumber.com/@#$-angel-number-meaning/"],
        '13': ["https://mattbeech.com/repeating-numbers/@#$-meaning/"],
        '14': ["https://www.mindbodygreen.com/articles/@#$-angel-number-meaning", "https://www.mindbodygreen.com/articles/@#$-angel-number"],
        '15': ["https://www.mindfulnessandjustice.org/angel-number-@#$-meaning/","https://www.mindfulnessandjustice.org/angel-number-@#$/"],
        '16': ["https://www.mindyourbodysoul.com/@#$-angel-number/","https://www.mindyourbodysoul.com/angel-number-@#$/"],
        '17': ["https://numerologynation.com/@#$-angel-number/","https://numerologynation.com/angel-number-@#$/"],
        '18': ["https://numerologysign.com/angel-number-@#$-meanings/"],
        '19': ["https://www.psychnewsdaily.com/@#$-angel-number-meaning/"], #manual csv
        '20': ["https://www.ryanhart.org/angel-number-@#$-meaning/"],
        '21': ["http://sacredscribesangelnumbers.blogspot.com/2019/01/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/12/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/05/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/04/angel-number-@#$.html"],
        '22': ["https://takanta.com/@#$-angel-number","https://takanta.com/angel-number-@#$"],
        '23': ["https://thesecretofthetarot.com/angel-number-@#$/"],
        '24': ["https://trustedpsychicmediums.com/angel-numbers/angel-number-@#$/"],
        '25': ["https://numerologycolumn.com/@#$-angel-number/","https://numerologycolumn.com/angel-number-@#$-numerology-meaning/","https://numerologycolumn.com/angel-number-@#$/"],
        '26': ["https://numeroscop.net/angel-numbers/@#$-angel-number.html"],
        '27': ["https://researchmaniacs.com/Numerology/Angel-Numbers/Angel-Number-@#$.html"],
        '28': ["https://www.sunsigns.org/angel-number-@#$-meaning/","https://www.sunsigns.org/angel-number-@#$"]}

remove_code = {'https://hiddennumerology.com':[{'orig':'<h3>Read the meaning of the other Angel Numbers</h3>', 'new':''}],
               'https://angelmanifest.com':[{'orig': '<h3>Other Angel Numbers:</h3>','new':''},
                                            {'orig': '<p>Also read:</p>','new': ''},
                                            {'orig': '<h2>Also Read:</h2>', 'new':''}],
               'https://numerologycolumn.com/':[{'orig':'<h3 class="h2">Recent Posts</h3>', 'new': ''}],
               'http://sacredscribesangelnumbers.blogspot.com': [{'orig':'<span ', 'new': '<p '},
                                                                 {'orig':'</span', 'new': '</p '}],
               'https://numerologycolumn.com/':[{'orig':'<h2>Related posts</h2>', 'new': ''}],
               'https://researchmaniacs.com/':[{'orig': '<br/><br/>','new':'</p><p>'},
                                            {'orig': '</br>','new': '<p>'},
                                            {'orig': '<b>', 'new':'<h4>'},
                                            {'orig': '</b>', 'new':'</h4>'}],
               'https://www.sunsigns.org': [{'orig': '<strong>See Also:</strong>','new':''}]
               }
default_redirected = {'www.mindyourbodysoul.com':'https://www.mindyourbodysoul.com',
                      'www.psychnewsdaily.com': 'https://www.psychnewsdaily.com',
                      'joynumber.com': 'https://joynumber.com'}