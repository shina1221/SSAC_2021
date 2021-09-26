
#import module basic.test_module로 임포트 하더라도 dir()로 확인해보면 네임스페이스에 test_module은 안들어감
#module_basic.test_module.PI
#module_basic.test_module.get_number()
#from module_basic.test_module import get_number

"""
#여기서 정의는 def

#패키지 import
  1) import 폴더 → X
  2) import 모듈
     → 모듈.정의
  3) import 모듈.정의 → X
  4) import 폴더.모듈
     → 폴더.모듈.정의
  5) import 폴더.폴더.모듈
     → 폴더.폴더.모듈.정의
  6) import 모듈 as 별칭
     → 별칭.정의
  7) import 폴더.폴더.폴더.모듈 as 별칭
     → 별칭.정의
  8) from 모듈 import 정의
     → 정의
  9) from 모듈 import 정의 as 별칭
     → 별칭
  10) from 폴더 import 모듈
     → 모듈.정의
  11) from 폴더 import 모듈 as 별칭
     → 별칭.정의
  12) from 폴더 import 폴더.모듈 → X
  13) from 폴더 import 모듈.정의 → X
  14) from 폴더.모듈 import 정의
    → 정의
  15) from 폴더.폴더 import 모듈
    → 모듈.정의
* 결론적
   - import 다음에는 (폴더.~~~.)모듈
   - from의 import는 모듈이나 정의만 
       ← 폴더.모듈, 모듈.정의 형태는 안됨
     - from (폴더.~~~.)모듈 import 정의
     - from (폴더.~~~.)폴더 import 모듈
     - from (폴더.~~~.)모듈 import 정의
   - as 별칭은 무조건 별칭으로



import module_basic.test_package.module.a
import module_basic.test_package.module.a.var_a

"""
