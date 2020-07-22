
# logParseTab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rootCMDARRAY CODEANDTIME DETAIL\n        root : DETAIL info\n        \n        info : CMDARRAY CODEANDTIME\n        '
    
_lr_action_items = {'DETAIL':([0,],[2,]),'$end':([1,3,5,],[0,-1,-2,]),'CMDARRAY':([2,],[4,]),'CODEANDTIME':([4,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'info':([2,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> DETAIL info','root',2,'p_all','logparser.py',28),
  ('info -> CMDARRAY CODEANDTIME','info',2,'p_info','logparser.py',36),
]
