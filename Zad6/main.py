import string
from decypher import Cypher

text = "\noljyn&skign&zlolj&ish&qnyh.&xlmiyxhyhgyj&qzsksixsmu&yosh,&qymyqm&xlnnlzl&osugoq&yuyh&zlolj,&qymyqm&nqiiq,&xgn&ilxssi&mqhlagy&kymqhsvgi&yh&nqumsi&zsi&kqjhgjsymh&nlmhyi.&mqixyhgj&jszsxgogi&ngi,&zlmyx&agqn&wyosi.&gohjsxsyi&myx.&kyooymhyiagy&yg.&kjyhsgn&agsi.&iyn,&mgooq&xlmiyagqh&nqiiq&agsi&ymsn,&zlmyx&kyzy&rgihl.&wjsmusooq&byo.&qosagyh&myx.&bgokghqhy&yuyh.&qjxg,&sm&ymsn&rgihl.&jtlmxgi&gh.&snkyjzsyh&q.&bymymqhsi&bshqy.&rgihl,&mgooqn&zsxhgn&wyosi&yg&kyzy&nloosi&kjyhsgn,&smhyuyj&hsmxszgmh,&xjqi&zqksvgi,&bsbqngi&yoynymhgn&iynkyj&msis,&qymyqm&bgokghqhy&yoyswymz&hyoogi,&qymyqm&oyl&osugoq.&kljhhshlj&yg.&xlmiyagqh&bshqy.&yoyswymz&qx.&ymsn,&qosagqn&oljyn&qmhy.&zqksvgi&sm.&bsbyjjq&agsi.&wygusqh&q.&hyoogi,&ktqiyoogi&bsbyjjq&mgooq&gh&nyhgi&bqjsgi&oqljyyh,&agsiagy&jghjgn,&qymyqm&snkyjzsyh,&yhsqn&gohjsxsyi&msis&byo&qgugy,&xgjqvshgj&gooqnxljkyj&gohjsxsyi&msis,&mqn&yuyh&zgs,&yhsqn&jtlmxgi,&nqyxymqi&hynkgi.&hyoogi&yuyh&xlmzsnymhgn&jtlmxgi.&iyn&agqn&iynkyj&osvyjl.&ish&qnyh&qzsksixsmu&iyn&myagy&iyz&skign,&m"
print(text)
print("\n")
textA="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. N" 
newtextA=""
for x in textA:
    if (x!=' '):
        newtextA+=x
print(textA)