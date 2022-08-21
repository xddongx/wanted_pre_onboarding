# wanted_pre_onboarding

# 요구사항 리스트
1. 채용공고 등록
2. 채용공고 수정
3. 채용공고 삭제
4. 채용공고
   * 목록
   * 검색
5. 채용 상세 페이지
6. 채용공고 지원 


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

![get 회사 리스트](https://user-images.githubusercontent.com/31644115/185795521-3e32062f-fbaa-4348-8400-8fa26766f004.JPG)

> GET /api/company/ID/

![get 회사 02](https://user-images.githubusercontent.com/31644115/185795468-bd34847c-d80c-4d5e-aac6-56c622a2785e.JPG)

> POST /api/company/

![post 회사](https://user-images.githubusercontent.com/31644115/185795545-236c2683-40e0-46c3-b286-8a92711229cf.JPG)

> PUT /api/company/ID/

![put 회사](https://user-images.githubusercontent.com/31644115/185795549-d7fb0a62-2aa3-410f-b36d-d41a56af3bf8.JPG)

> DELETE /api/company/ID/

![delete 회사](https://user-images.githubusercontent.com/31644115/185797650-d7ec3e02-22df-4bef-a107-b2def7fb83c7.JPG)

## 사용자 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/user/|모든 사용자 조회|
|GET|/api/user/ID/|특정 사용자 조회|
|POST|/api/user/|새 사용자 추가|
|PUT|/api/user/ID/|특정 사용자 갱신|
|DELETE|/api/user/ID/|특정 사용자 삭제|

> GET /api/user/

![get 사용자 리스트](https://user-images.githubusercontent.com/31644115/185795573-94b23498-6637-4a95-8697-f0830da19959.JPG)

> GET /api/user/ID/

![get 사용자](https://user-images.githubusercontent.com/31644115/185795558-0c007a7e-d97f-4e31-b13f-f76e37b2948c.JPG)

> POST /api/user/

![post 사용자](https://user-images.githubusercontent.com/31644115/185795585-7bb0d779-f659-4042-896b-7289d1a78903.JPG)

> PUT /api/user/ID/

![put 사용자](https://user-images.githubusercontent.com/31644115/185795598-8e849f1c-9fa4-44a2-925c-4aac70c57952.JPG)

> DELETE /api/user/ID/

![delete 유저](https://user-images.githubusercontent.com/31644115/185797665-e5dd7bf4-9ecb-4358-b5c0-27acf3acf8a8.JPG)

## 채용공고 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/job_posting/|모든 채용공고 조회|
|GET|/api/job_posting/ID/|특정 채용공고 조회|
|POST|/api/job_posting/|새 채용공고 추가|
|PUT|/api/job_posting/ID/|특정 채용공고 갱신|
|DELETE|/api/job_posting/ID/|특정 채용공고 삭제|

> 4-1.채용공고 목록
<br>GET /api/job_posting/

![get 채용공고 리스트](https://user-images.githubusercontent.com/31644115/185795626-8917baa6-7691-4464-bbfe-56a411824d63.JPG)

> 5.채용공고 상세 페이지
<br>GET /api/job_posting/ID/

![get 채용공고](https://user-images.githubusercontent.com/31644115/185795618-7c3752b4-d33c-4698-a591-358cfc84c868.JPG)

> 1.채용공고 등록
<br>POST /api/job_posting/

![post 채용공고](https://user-images.githubusercontent.com/31644115/185795638-7576f2d3-c00e-4f12-a768-5192a6cfc16a.JPG)

> 2.채용공고 수정
<br>PUT /api/job_posting/ID/

![put 채용공고](https://user-images.githubusercontent.com/31644115/185795645-f3f12203-0b85-41d8-b5af-b3b3075281e9.JPG)

> 3.채용공고 삭제
<br>DELETE /api/job_posting/ID/

![delete 최용공고](https://user-images.githubusercontent.com/31644115/185797690-deecffa9-7275-48fa-85fd-1e45fb5ba6b1.JPG)

## 지원 CRUD
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/application/|모든 지원 조회|
|GET|/api/application/ID/|특정 지원 조회|
|POST|/api/application/|새 지원 추가|
|PUT|/api/application/ID/|특정 지원 갱신|
|DELETE|/api/application/ID/|특정 지원 삭제|

> 6.채용공고 지원 목록
<br>GET /api/application/

![get 지원 리스트](https://user-images.githubusercontent.com/31644115/185797701-579b77c1-1859-44ea-a399-e14fe7c8004a.JPG)

> GET /api/application/ID/

![get 지원](https://user-images.githubusercontent.com/31644115/185797715-3bbe6af7-35a0-420a-8426-d4c3d64b919f.JPG)

> POST /api/application/

![post 지원](https://user-images.githubusercontent.com/31644115/185795672-fec1c2b8-8e7d-45b2-89a8-770d4a9e4315.JPG)

> PUT /api/application/ID/

![put 지원](https://user-images.githubusercontent.com/31644115/185797724-f1d11584-99e2-4a2d-b8f2-f34531d57a73.JPG)

> DELETE /api/application/ID/

![delete 지원](https://user-images.githubusercontent.com/31644115/185797739-790df586-31ca-414f-a07b-df02b770450b.JPG)

## 채용공고 검색(회사명, 채용내용 사용기술)
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/some/url?search="검색 단어"|검색 단어가 포함된 채용공고 조회|

> 4-2.채용공고 검색
<br>GET /api/some/url?search="검색 단어"

![get search](https://user-images.githubusercontent.com/31644115/185795657-391240fb-6ec4-4247-9c6a-655e1d984f28.JPG)


