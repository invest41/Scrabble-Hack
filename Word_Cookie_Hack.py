#1.0 
print(f'''
+------------------------------+
+ Scrabble or Word Cookie Hack +
+------------------------------+

''')

success = f'''
SUCCESSFUL UPLOAD
   '''


#2.0
df = open('Cookie.txt','w')
#df.close()
#df = open('Cookie.txt','a')


#3.0
import nltk, random, time
fwl = nltk.corpus.words.words()



#4.0
word, co, lw, key, inertia, lst2 = input('Input the letters on your tile(s)... ').lower().strip().replace(' ',''), 0, int(input('How many letter word? ')),input('Show Background Result? ').startswith('y'), None, []


# 5.0
try:
 assert key
 lock = False
except:
 lock = 1
 print('''

+---------------------------+
+ Background Work is Hidden +
+---------------------------+

''')



hmm = 0



#6.0
run, ref, stop, cross, uw, brk_exp = len(fwl), len(word), 0, [], word[:], 0
while True:
 if stop == ref**5 or len(lst2)>=20: break
 
 
 
 #6.1
 if co>0:
  uw = list(uw)
  random.shuffle(uw)
  uw = ''.join(uw)
  word = uw[:]
  if not word in cross: cross.append(word)
  
  #6.2
  else:
   brk_exp += 1
   if not brk_exp == len(cross): continue
   print('\nEnd...')  #No Result...')
   break
   

  brk_exp = 0
  
  #6.3
  #time.sleep(0.3)
  if stop%5==0: print('Processing...')
  stop+=1
 
 
 
 #6.4 
 for dw in fwl:
  co+=1
  
  #6.5
  conf = []
  if not len(dw)==lw: continue
 
  #6.6
  short = len(word)<lw
  if len(word)==lw: pass
  elif short: word = word + word[random.randint(0,len(word)-1)]
  elif not short:
   word = word[:lw]
  
  #6.7 Main Logic 
  for c in word:
   if c in dw:
    if word.count(c) == dw.count(c):
     conf.append(True)

  #6.8
  if not lock: #Show Background Result
   if stop <5:
    if run%(co/10)==0: pass #For Future Ideas
  if not inertia:	
   df.write(f'''Your {lw} Letter Words:

''')
   inertia = True
  
  #6.9 Confirm and Filter
  if len(conf)==len(word)==len(dw):
   if not lock: print(f'\n\n{dw}{success}')
   if not dw in lst2:
    df.write(f'{dw}, nltk.corpus.words.words()[{co-1}]\n')
    lst2.append(dw)
    
    #5.4 - Monitor Progress
    df.close()
    df = open('Cookie.txt','a')
    if lock: print(success)



#7.0
df.write(f'''
{len(lst2)} Words''')
df.close()
print('\n\nDone!')
