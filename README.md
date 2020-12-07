# collaborative-text-editor

i am going to try implementing the backend using django
- for websocket connections ill use django-channels
- for merging and conflict resolution i have decided to try CRDT.

some great links to study about modelling the problems of syncronisation  of state of different machines -
- https://scattered-thoughts.net/writing/causal-ordering/
- https://sergeiturukin.com/2017/06/26/hybrid-logical-clocks.html

some github repos to checkout for python implementations -  
* https://github.com/anshulahuja98/python3-crdt  
* https://github.com/linkdd/link.crdt  

some repos to checkout the applications built out of CRDT- 
* https://github.com/Xuzhiqian/WYJPad

## CRDTs
- stands for conflict free resolution datatype
- has two basic properties
- commutative - means the order doesn matter the changes are applied
- idempotent- no matter how many times you  apply it, it still remains the same.

- some implementations 
    - G counter
    - PN Counter
    - G-Set
    - 2P-Set

