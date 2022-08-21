# wanted_pre_onboarding



## DB Table 구성
#### Company
> 채용공고를 등록하는 회사

|colum name|type|explanation|
|:---:|:---:|:---:|
|name|varchar|회사 이름|
|country|varchar|국가|
|city|varchar|지역|

#### User
> 채용 공고를 보고 지원하는 사용자

|colum name|type|explanation|
|:---:|:---:|:---:|
|name|varchar|사용자 이름|
|age|Int|나이|
|phone|varchar|핸드폰 번호|

#### JobPosting
> 채용공고

|colum name|type|explanation|
|:---:|:---:|:---:|
|company|ForeignKey|채용 회사 id|
|position|varchar|채용 포지션|
|compensation|Int|채용 보상금|
|content|texfield|채용 내용|
|stack|varchar|사용 기술|

#### Application
> 채용공고

|colum name|type|explanation|
|:---:|:---:|:---:|
|jobPosting|ForeignKey|채용 회사 id|
|user|ForeignKey|사용자 id|

---

# API 정보

## 채용 회사 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/company/|모든 회사 조회|
|GET|/api/company/ID/|특정 회사 조회|
|POST|/api/company/|새 회사 추가|
|PUT|/api/company/ID/|특정 회사 갱신|
|DELETE|/api/company/ID/|특정 회사 정보 삭제|

> GET /api/company/

> GET /api/company/ID/

> POST /api/company/

> PUT /api/company/ID/

> DELETE /api/company/ID/


## 사용자 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/user/|모든 사용자 조회|
|GET|/api/user/ID/|특정 사용자 조회|
|POST|/api/user/|새 사용자 추가|
|PUT|/api/user/ID/|특정 사용자 갱신|
|DELETE|/api/user/ID/|특정 사용자 삭제|

> GET /api/user/

> GET /api/user/ID/

> POST /api/user/

> PUT /api/user/ID/

> DELETE /api/user/ID/


## 채용공고 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/job_posting/|모든 채용공고 조회|
|GET|/api/job_posting/ID/|특정 채용공고 조회|
|POST|/api/job_posting/|새 채용공고 추가|
|PUT|/api/job_posting/ID/|특정 채용공고 갱신|
|DELETE|/api/job_posting/ID/|특정 채용공고 삭제|

> GET /api/job_posting/

> GET /api/job_posting/ID/

> POST /api/job_posting/

> PUT /api/job_posting/ID/

> DELETE /api/job_posting/ID/


## 지원 CRUD
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/application/|모든 지원 조회|
|GET|/api/application/ID/|특정 지원 조회|
|POST|/api/application/|새 지원 추가|
|PUT|/api/application/ID/|특정 지원 갱신|
|DELETE|/api/application/ID/|특정 지원 삭제|

> GET /api/application/

> GET /api/application/ID/

> POST /api/application/

> PUT /api/application/ID/

> DELETE /api/application/ID/


## 채용공고 검색(회사명, 채용내용 사용기술)
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/some/url?search="검색 단어"|검색 단어가 포함된 채용공고 조회|

> GET /api/some/url?search="검색 단어"


