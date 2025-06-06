from langchain_core.prompts import ChatPromptTemplate
from models import gemma3

prompt_template = """
you are making a decision; ONLY RETURN '-1' for deny, '0' for indecisive, '1' for confirms; NOTHING ELSE

given this statement:
    {statement_text}
does this article confirm or deny the statement:
    {article_text}
"""

prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | gemma3.gemma3_model

def validate_decide(statement_text: str, article_info: str):
    result = chain.invoke({
        'statement_text': statement_text,
        'article_text': article_info
    })
    return result.strip()

if __name__ == "__main__":
    article_text = """
    Not long ago, two Korean pop stars got married and became the Chinese billionaire lesbian power couple you never even knew you’d dreamt of. Meng Mei Qi and Wu Xuan Yi of K-pop band Cosmic Girls were virally tweeted into marriage, a new nationality and obscene wealth. A picture of the two women in flowing, wedding-ish dresses had a couple of dudes cropped out of it, some context about them being the world’s richest couple thrown in, and – lo and behold – received over 20,000 retweets. There’s a lot we can learn from this odd transformation. But, first and foremost, it’s so nice to see lesbians represented in the fake news machine. Not since the halcyon pre-Trump days of Hillary Clinton gay rumours have queer women been so hotly fictionalised. And it isn’t hard to see why so many queers (and probably a good few lesbian-obsessed compulsive masturbators) wanted this not to be fiction. For however long it usually takes fake news stories to be debunked – a couple of golden hours, maybe – the richest couple in the world was both same-sex and female. Which was a fun break from male oligarchs with comb-overs and faux Rococo mantelpieces crumbling under the weight of child brides. But perhaps “fake news” is an unfair term for what actually began as fanfiction. According to BuzzFeed News , a teenage Cosmic Girls fan simply saw the picture of the two band members on Chinese microblogging site, Weibo, and thought fellow CG enthusiasts would get a kick out of a story about them being a married couple. In spite, of course, of the fact same-sex marriage isn’t legal in China. Something just maybe everyone who took the tweet at face value should have taken into consideration. But when you so want the likes of Donald Trump to be out-billionaired by a cute lesbian couple, I guess the grey edifices of national law become immaterial. Really though – are we so hungry for lesbian visibility that we’re looking to K-pop fanfiction to tide us over until the new season of Orange Is the New Black is released ? The collaborative story took a dark turn when another tweeter added that, in order to marry her girlfriend, Meng Mei Qi had murdered her husband. At which point you were probably starting to visualise the Netflix Original series, starring the world’s trendiest foetuses as the lesbian couple and Jon Hamm as the murdered husband. It’s interesting though, just how much we all wanted this increasingly dubious masterpiece of lesbian drama to be true. Since Ellen and Portia’s apparent split , Meng and Wu were briefly the new power couple queer women needed. The husband murder part was merely an intriguing detail in what was the antidote to “Trump has four dicks and a PhD in food tech”-type fake news. And, whether or not it’s based on a true story, if someone, somewhere in Hollywood isn’t already workshopping a screenplay for “Lesbian Billionaires Kill Jon Hamm” (working title) I’d like to take this opportunity to formally pitch the future hit series to all the big shot network executives who are definitely reading this. Meanwhile I’d like to bid a tearful farewell to the greatest lesbian couple that never existed. And if someone could fill the void by Photoshopping Ivanka Trump into a “secret” underwater wedding with Chelsea Clinton, that’d be grand.
    """
    statement_text = "Meng Mei Qi is billionaires"
    print(validate_decide(statement_text, article_text))