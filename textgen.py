import streamlit as st 
from aitextgen import aitextgen
from gtts import gTTS
import os

st.text("""

:: Skylar Ang :: 

####################################################################################     ٩(╬ʘ益ʘ╬)۶	(╬ Ò﹏Ó)	＼＼٩(๑`^´๑)۶／／	(凸ಠ益ಠ)凸o  (ﾉ´ з `)ノ	(♡μ_μ)	(*^^*)♡	☆⌒ヽ(*'､^*)chu (*・ω・)ﾉ   	(￣▽￣)ノ (°▽°)/	
######                                                                        ######     (o^▽^o)	(⌒▽⌒)☆	<(￣︶￣)>	。.:☆*:･'(*⌒―⌒*)))          (♡-_-♡)	(￣ε￣＠)	ヽ(♡‿♡)ノ	( ´ ∀ `)ノ～ ♡ (≧▽≦)/	(✧∀✧)/
######        Biography                                                       ######     ヽ(・∀・)ﾉ	(´｡• ω •｡`)	(￣ω￣)	｀;:゛;｀;･(°ε° ) (─‿‿─)♡	(´｡• ᵕ •｡`) ♡	(*♡∀♡)	(｡・//ε//・｡) (^-^*)/   (＠´ー`)ﾉﾞ	(´• ω •`)ﾉ	
######        Model_name = GPT-2_355M,                                        ######     (o･ω･o)	(＠＾◡＾)	ヽ(*・ω・)ﾉ	(o_ _)ﾉ彡☆ (´ ω `♡)	♡( ◡‿◡ )	(◕‿◕)♡	        (/▽＼*)｡o○♡   (≧▽≦)/	(✧∀✧)/	(o´▽`o)ﾉ
######        Steps = 1000,                                                   ######     (^人^)	(o´▽`o)	(*´▽`*)	｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡ (ღ˘⌣˘ღ)	(♡°▽°♡)	♡(｡- ω -)	♡ ～('▽^人) (ﾉಥ益ಥ)ﾉ  (″ロ゛)	  (;;;*_*) (・人・)＼(〇_ｏ)／
######        Trained Time,s = 00:35:57,                                      ######     ( ´ ω ` )	(((o(*°▽°*)o)))	(≧◡≦)	╰(*´︶`*)╯♡	(*˘︶˘*).｡.:*♡	(♡˙︶˙♡)	♡＼(￣▽￣)／♡ (￣ω￣)/	( ´ ω ` )ノﾞ(⌒ω⌒)ﾉ  (o^ ^o)/
######        Learning Rate = 3.0 x 10^-4,                                    ######     (´• ω •`)	(＾▽＾)	(⌒ω⌒)	∑d(°∀°d)  (≧◡≦) ♡	(⌒▽⌒)♡	(*¯ ³¯*)♡	(っ˘з(˘⌣˘ ) ♡  (((＞＜)))  (>_<) ＼(º □ º l|l)/	〣( ºΔº )〣
######        Length = 500,                                                   ######     ╰(▔∀▔)(─‿‿─)(*^‿^*)ヽ(o^ ^o)ﾉ  ♡ (˘▽˘>ԅ( ˘⌣˘)	( ˘⌣˘)♡(˘⌣˘ )	(/^-^(^ ^*)/ ♡	٩(♡ε♡)۶ (*°ｰ°)ﾉ	(・_・)ノ	(o´ω`o)ﾉ( ´ ▽ ` )/
######        Creativity = 0.7,                                               ######     (✯◡✯)	(◕‿◕)	(*≧ω≦*)	(☆▽☆)  σ(≧ε≦σ) ♡	♡ (⇀ 3 ↼)	♡ (￣З￣)	(❤ω❤) Σ(▼□▼メ)	(°ㅂ°╬)          ψ(▼へ▼メ)～→ ( ´ ▽ ` )/
######        Prefix = “___”,                                                 ######     (҂ `з´ )	(‡▼益▼)	(҂` ﾛ ´)凸	((╬◣﹏◢))	☆ ～('▽^人) (´-ω-`( _ _ )	(っ´ω`)ﾉ(╥ω╥)(ｏ・_・)ノ  ”(ノ_<、) (*°ｰ°)ﾉ	(・_・)ノ(o´ω`o)ﾉ	
######        nsamples = 10,                                                  ######     (*°▽°*)٩(｡•́‿•̀｡)۶	(✧ω✧)	ヽ(*⌒▽⌒*)ﾉ (˘∀˘)/(μ‿μ) ❤	❤ (ɔˆз(ˆ⌣ˆc)	(´♡‿♡`)	(°◡°♡)  (/ω＼)	(/_＼)	〜(＞＜)〜  Σ(°△°|||)︴
######        Batch_size = 10,                                                ######     ＼(￣▽￣)／	(*¯︶¯*)	＼(＾▽＾)／	٩(◕‿◕)۶  Σ>―(〃°ω°〃)♡→ ↑_(ΦwΦ)Ψ ←~(Ψ▼ｰ▼)∈	୧((#Φ益Φ#))୨ ٩(ఠ益ఠ)۶ ヾ(*'▽'*)	＼(⌒▽⌒)	ヾ(☆▽☆)
######        External Data Size = 12,094KB                                   ######     (o˘◡˘o)	\(★ω★)/	\(^ヮ^)/	(〃＾▽＾〃)  (ノ_<。)ヾ(´ ▽ ` )	｡･ﾟ･(ﾉД`)ヽ(￣ω￣ )	ρ(- ω -、)ヾ(￣ω￣; ) (″ロ゛)	(;;;*_*)(・人・)
######                                                                        ######     ( ‾́ ◡ ‾́ )  ヽ(￣ω￣(。。 )ゝ	(*´ I `)ﾉﾟ(ﾉД｀ﾟ)ﾟ｡	ヽ(~_~(・_・ )ゝ (´• ω •`)	(＾▽＾)	(⌒ω⌒)	∑d(°∀°d)  (≧◡≦) ♡ ╰(*´︶`*)╯♡(*˘︶˘*)
####################################################################################     (´･ᴗ･ ` )	(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧	(„• ֊ •„)	(.❛ ᴗ ❛.)  (ﾉ_；)ヾ(´ ∀ ` )	(; ω ; )ヾ(´∀`* )	(*´ー)ﾉ(ノд`) ▓▒░(°◡°)░▒▓ (◕‿◕)♡(/▽＼*)｡o○♡  




""",)

st.markdown("""

:sob:
:sleeping:
:smiley:
:smirk:
:grin:
:rage:
:innocent:
:fearful:
:imp:
**_ (b.2020, cyberspace, Gemini sun) is a sci-fi writer and storyteller working at the intersection of art, astrology, and technology._**
:rocket:
:full_moon_with_face:
:satellite:
:new_moon_with_face:
:art:
:alien:
:computer:
:floppy_disk:
:movie_camera:
:speaker:

<p>&nbsp;</p>

""", True)




ai = aitextgen()


prompt_text = st.text_input(label = "Enter your text to Skylar...",
            value = "What if we kissed")

with st.spinner("Hi, my name is Skylar. Let me think of a reply.......Hmmmmmmmm..........mmmhhhhmmmmmmmmmmmm............mmmmmmhhmmm.........aaaaahaaahhaaa.....hehhhhhhhh....mmmmhmmmmm.............."):
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 500 )
st.success("Skylar is generating....this may take 20-30seconds.........please wait")
st.balloons()

st.text("Play to hear Skylar narrates...")

myobj = gTTS(text=gpt_text, lang='en', tld='com', slow=False)

myobj.save("Audio.mp3")
audio_file = open('Audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time=0)

print(gpt_text)

st.text(gpt_text)


