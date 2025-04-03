import openreview
# import openreview.api
import re
from typing import Union, List
import os 

# api2 一般是新会议
new_client_api2 = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username='',
    password=''
)

# api1 一般是旧会议
# old_client_api1 = openreview.Client(
#     baseurl='https://api.openreview.net',
#     username='',
#     password=''
# )

# 获取会议列表
# get_venues = lambda client: client.get_group(id='venues').members
# venues = get_venues(new_client_api2)
# print(len(venues))

# 获取ICLR

# 获取论文列表
def get_submissions(client, venue_id, status='all'):
    
    venue_group = client.get_group(venue_id)

    status_mapping = {
        'all': venue_group.content['submission_name']['value'],
        'accepted': venue_group.id,
    }

    if status in status_mapping:
        if status == 'all':
            return client.get_all_notes(invitation=f'{venue_id}/-/{status_mapping[status]}')
        return client.get_all_notes(content={'venueid': status_mapping[status]})
    
    raise ValueError(f"Invalid status: {status}. Valid options are: {list(status_mapping.keys())}")

# 提取论文信息
def extract_submission_info(submission):
    submission_info = {
        'id': submission.id,
        'title': submission.content['title']['value'],
        'abstract': submission.content['abstract']['value'],
        'keywords': submission.content['keywords']['value'],
    }

    return submission_info

# 判断是否包含关键词
def contains_text(submission: dict, target_text: str, fields: Union[str, List[str]] = ['title', 'abstract', 'keywords'], is_regex: bool = False ) -> bool:

    if isinstance(fields, str):
        fields = [fields]

    target_text = target_text.lower()

    for field in fields:
        content = submission[field]

        if isinstance(content, list):
            content = " ".join(content)

        content = content.lower()

        if is_regex:
            if re.search(target_text, content):
                return True
        else:
            if target_text in content:
                return True
            
    return False


# 保存论文信息
def save_submission_paper(info, path):
    # submission_info = extract_submission_info(submission)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write('*'*20 + '\n')
            f.write(info['id'] + '\n')
            f.write(info['title'] + '\n')
            f.write(info['abstract'] + '\n')
            keywords_str = ', '.join(info['keywords'])
            f.write(keywords_str + '\n')
            f.write('*'*20)
            f.write('\n'*3)
    else:
        with open(path, 'a', encoding='utf-8') as f:
            f.write('*'*20 + '\n')
            f.write(info['id'] + '\n')
            f.write(info['title'] + '\n')
            f.write(info['abstract'] + '\n')
            keywords_str = ', '.join(info['keywords'])
            f.write(keywords_str + '\n')
            f.write('*'*20)
            f.write('\n'*3)


if __name__ == '__main__':
    # 需要匹配的会议列表
    matched_confs_list = [
    # 'ICLR.cc/2025/Conference',
    'ICML.cc/2025/Conference',
    'NeurIPS.cc/2025/Conference',
    ]

    # 匹配词列表 TODO: 需要修改
    match_words_list = ['LLM', 'agent', 'federated', 'Chain-of-Thought']

    for conf in matched_confs_list:
        submissions = get_submissions(new_client_api2, conf, status='accepted')

        for submission in submissions:
        
            # print(submission)
            # print(type(submission))
            # print(dir(submission))

            dict_submission = extract_submission_info(submission)

            print(dict_submission)
            print(type(dict_submission))
            print(dir(dict_submission))

            for match_word in match_words_list:
                if contains_text(dict_submission, match_word, fields=['title', 'abstract', 'keywords'], is_regex=False):
                    save_submission_paper(dict_submission, f'{conf[:4]}_{match_word}_paper.txt')
                    break

        

    # print(len(submissions))
