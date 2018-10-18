#!/usr/bin/env python3

import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..', 'blog'))


def Replace(post, template):
    result = template
    if 'content' in post:
        result = result.replace('[[[content]]]', post['content'])
    result = result.replace('[[[title]]]', post['title'])
    result = result.replace('[[[path]]]', post['path'])
    result = result.replace('[[[datestamp]]]', post['datestamp'])
    result = result.replace('[[[datehuman]]]', post['datehuman'])
    result = result.replace('[[[daterss]]]', post['daterss'])
    result = result.replace('[[[descriptionshort]]]', post['descriptionshort'])
    result = result.replace('[[[descriptionlong]]]', post['descriptionlong'])
    result = result.replace('[[[author]]]', post['author'])
    result = result.replace('[[[image]]]', post['image'])
    result = result.replace('[[[imagealt]]]', post['imagealt'])
    return result


def ReplaceEachSections(template, num_sections, posts):
    for i in range(0, num_sections):
        parts = template.split('[[[each%d]]]' % (i+1))
        head = parts[0]
        parts = parts[1].split('[[[%deach]]]' % (i+1))
        replaceable = parts[0]
        tail = parts[1]
        template = head
        for post in posts:
            template += Replace(post, replaceable)
        template += tail
    return template


def OutputPost(post, older_posts):
    with open(os.path.join(ROOT_DIR, '_posts', post['path'] + '.html')) as content_file:
        with open(os.path.join(ROOT_DIR, '_templates', 'post.html')) as template_file:
            template = template_file.read()
            content = content_file.read()
    post['content'] = content
    result = ReplaceEachSections(template, 1, older_posts)
    result = Replace(post, result)
    output_dir = os.path.join(ROOT_DIR, post['path'])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(os.path.join(output_dir, 'index.html'), 'w') as post_file:
        post_file.write(result)


def OutputAllPostTemplate(template_spec, posts):
    with open(os.path.join(ROOT_DIR, '_templates', template_spec['file'])) as template_file:
        template = template_file.read()
    template = ReplaceEachSections(template, template_spec['each_count'], posts)
    template = template.replace('[[[mostrecentdate]]]', posts[0]['daterss'])
    with open(os.path.join(ROOT_DIR, template_spec['outpath']), 'w') as out_file:
        out_file.write(template)


if __name__ == '__main__':
    index = None
    with open(os.path.join(ROOT_DIR, '_posts', 'index.json')) as index_file:
        index = json.load(index_file)
    all_posts = index['posts']
    while all_posts:
        newest_post = all_posts[0]
        all_posts = all_posts[1:]
        OutputPost(newest_post, all_posts)
    for all_post_template in index['allposttemplates']:
        OutputAllPostTemplate(all_post_template, index['posts'])
