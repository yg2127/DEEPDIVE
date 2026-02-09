# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

파이썬을 포함한 다양한 공부를 하는 학습용 저장소. 구름(goorm) DEEPDIVE 부트캠프 + 인프런 Python 강의 실습 코드를 관리한다.

## Repository Structure

- `DeepDive/` - 구름 DEEPDIVE 부트캠프 실습 (날짜별 폴더: `0119/`, `0126/`, `0203/`, `0207/`)
  - 데이터 분석 관련: pandas, plotly, streamlit 등
- `inflearn_python1/` - 인프런 파이썬 입문 강의
  - `source_code/` - 강의 제공 소스코드 (chapter별)
  - `mycode/` - 직접 작성한 실습 코드 (강의 번호 기준 파일명: `6_7_8.py`, `10_11.py` 등)
- `inflearn_python2/` - 인프런 파이썬 중급 강의
  - `source_file/` - 강의 제공 소스코드 (`p_chapter*`)
  - `my_code/` - 직접 작성한 실습 코드

## Conventions

- 실습 파일명은 강의 번호 기반: `{시작번호}_{끝번호}.py` (예: `14_15.py`)
- `source_code`/`source_file` 폴더는 강의 원본이므로 수정하지 않는다
- `mycode`/`my_code` 폴더가 사용자 작업 공간

## Running Code

```bash
python3 <파일경로>
```

- Streamlit 앱: `streamlit run <파일경로>`

## Language

- 한국어로 응답

## Global Rules

- Write commit messages in English, conventional commits (`feat:`, `fix:`, `refactor:`, `docs:`, `chore:`)
- Use `pip` or `conda` for Python packages
- Never modify `source_code`/`source_file` directories (lecture originals)