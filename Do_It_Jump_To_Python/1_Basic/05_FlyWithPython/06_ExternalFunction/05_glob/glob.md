# glob( pahtname ) - 디렉토리에 있는 파일들을 리스트로 만들기
파일을 읽고 쓰는 기능이 있는 프로그램을 만들다 보면 특정 디렉토리에 있는 파일 이름을 모두 알아야 하는 경우가 있음.  
glob 모듈은 디렉토리 안의 파일들을 읽어서 돌려준다.  
`*`, `?`등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.

```
>>> import glob
>>> glob.glob('/*')
['/home', '/usr', '/net', '/bin', '/installer.failurerequests', '/Network', '/sbin', '/etc', '/var', '/Library', '/System', '/private', '/Users', '/Applications', '/dev', '/Volumes', '/tmp', '/cores']
```