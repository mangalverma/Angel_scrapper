remove_attribute = {'https://angelnumber.org': {'id': ['M381992ScriptRootC303780'],'class': ['hm-related-posts','cat-links']},
                    'https://angelmanifest.com': {'class': ['wp-block-embed is-type-wp-embed is-provider-angel-manifest wp-block-embed-angel-manifest','entry-meta','ct-breadcrumbs']},
                    'https://www.angelsnumbers.com/':{'id': ['le_body_row_8'], 'class': ['op-custom-html-block','breadcrumb-style-7']},
                    'https://www.coolastro.com/':{'id': ['comments','ez-toc-container'], 'class': ['entry-meta','relpost-thumb-wrapper']},
                    'https://divineangelnumbers.com/':{'id':['comments', 'grow-me-in-content-recs-root'],'class': ['uagb-toc__wrap', 'entry-category-icon', 'entry-meta clear', 'social-share-icons', 'has-background','author-box clear', 'entry-related clear', 'wp-block-image']},
                    'https://www.guardian-angel-reading.com/': {'id': ['share'],'class': ['related-articles fixedfont','homeform homeform--og ', 'byline author vcard']},
                    'https://hiddennumerology.com/': {'id': ['ez-toc-container', 'dpsp-content-bottom', 'grow-me-in-content-recs-root'], 'class':['purplebox','pinkbox','yellowbox', 'emalsubinpt', 'saboxplugin-tab', 'dpsp-share-text ', 'navigation post-navigation']}}
page_xpath = [('https://hiddennumerology.com',"//main[@id='main']"), #10
              ('https://www.adviseastro.com',"//div[@class='inside-article']"), #1
              ('https://angelmanifest.com',"//div[@class='hero-section']|//div[@class='entry-content']"), #2
              ('https://angelnumber.org/', '//*[@id="main"]'), #4
              ('https://angelnumbersmeaning.com//', '//*[@id="main"]'),#5
              ('https://www.angelsnumbers.com/', '//*[@id="content_area"]'), #6
              ('https://www.coolastro.com/','//*[@id="primary"]'), #7
              ('https://divineangelnumbers.com/','//*[@id="main"]'), #8
              ('https://www.guardian-angel-reading.com/','//*[@id="sticky-anchor"]/div/main')] #9
ignore_tag_by_domain = {'https://angelmanifest.com': ['ul']}
page_wise_delimeter = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
para_wise_delim = '@@@@@@@@@@@@@@@@@@@'
ignore_site_num = [1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
url_patterns = {'1':  ["https://www.adviseastro.com/angel-number-@#$-meaning-and-symbolism/"],
        '2':  ['https://angelmanifest.com/angel-number-@#$/'],
        '3':  ["https://angelnumber.me/@#$-meaning/"],
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
        '14': ["https://www.mindbodygreen.com/articles/@#$-angel-number","https://www.mindbodygreen.com/articles/@#$-angel-number-meaning"],
        '15': ["https://www.mindfulnessandjustice.org/angel-number-@#$/","https://www.mindfulnessandjustice.org/angel-number-@#$-meaning/"],
        '16': ["https://www.mindyourbodysoul.com/@#$-angel-number/","https://www.mindyourbodysoul.com/angel-number-@#$/"],
        '17': ["https://numerologynation.com/@#$-angel-number/","https://numerologynation.com/angel-number-@#$/"],
        '18': ["https://numerologysign.com/angel-number-@#$-meanings/"],
        '19': ["https://www.psychnewsdaily.com/@#$-angel-number-meaning/"],
        '20': ["https://www.ryanhart.org/angel-number-@#$-meaning/"],
        '21': ["http://sacredscribesangelnumbers.blogspot.com/2019/01/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/12/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/05/angel-number-@#$.html","http://sacredscribesangelnumbers.blogspot.com/2018/04/angel-number-@#$.html"],
        '22': ["https://takanta.com/@#$-angel-number","https://takanta.com/angel-number-@#$"],
        '23': ["https://thesecretofthetarot.com/angel-number-@#$/"],
        '24': ["https://trustedpsychicmediums.com/angel-numbers/angel-number-@#$/"],}

remove_code = {'https://hiddennumerology.com':['<h3>Read the meaning of the other Angel Numbers</h3>'],'https://angelmanifest.com':['<h3>Other Angel Numbers:</h3>','<p>Also read:</p>','<h2>Also Read:</h2>']}