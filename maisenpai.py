import discord


class chatbot(discord.Client):
    
    async def on_ready(self):
       
        game = discord.Game("hitomi.la")

        
        
        await client.change_presence(status=discord.Status.online, activity=game)

        

    
    async def on_message(self, message):
        
        if message.author.bot:
            return None
        
        #1번  
        if message.content == "마이선배 안녕" :
            
            channel = message.channel
            
            hello = "안녕."
            
            await channel.send(hello)
            return None

        #2번
        if message.content == "마이선배 뭐해?" :

            channel = message.channel
            
            wut = "뭐 하긴,너랑 얘기하고 있지."
            
            await channel.send(wut)
            return None

        #3번
        if message.content == "마이선배 생일은?" :

            channel = message.channel
            
            birthday = "12월 2일이야."
            
            await channel.send(birthday)
            return None 
        
        from datetime import datetime

        #4번
        if message.content == "마이선배 가슴 만지게 해줘" :
            
            channel = message.channel

            oppai = "하아?벼,변태!"
            
            await channel.send(oppai)
            return None 
        
        from datetime import datetime 

        #5번
        if message.content == "마이선배 손" :
            
            channel = message.channel

            dog = "내가 개로 보이는 거야?"
            
            await channel.send(dog)
            return None

        #6번
        if message.content == "마이선배 키" :
            
            channel = message.channel

            height = "그런 건 실례라고?"
            
            await channel.send(height)
            return None

         #7번
        if message.content == "마이선배 오늘 팬티 색" :
            
            channel = message.channel

            pantsu = "무,무슨 소리야...!"
            
            await channel.send(pantsu)
            return None  




if __name__ == "__main__":
    
    client = chatbot()

    client.run("NzcxMTY4NjcyOTY1NDU5OTY5.X5oMyw.KO3PuzupYkp4Cn_vboJ8yLLrVs4") 
