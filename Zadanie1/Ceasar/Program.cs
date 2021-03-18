using Ceasar.Model;
using Ceasar.Services;
using SimpleInjector;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ceasar
{
    class Program
    {
        static void Main(string[] args)
        {
            Container container = new Container();
            CeasarDecryptor ceasarDecryptor = new CeasarDecryptor();
            TextService textService = new TextService();
            List<string> textsToDecrypt = new List<string>();
            List<Text> texts = new List<Text>();

            container.Options.ResolveUnregisteredConcreteTypes = true;
            container.Register<ITextService, TextService>();
            container.Verify();
            textService = container.GetInstance<TextService>();

            Task.Run(async () =>
            {
                texts = await textService.GetTexts();
                textsToDecrypt = ceasarDecryptor.GetTexts(texts);
            });
            
            foreach(string text in textsToDecrypt)
            {
                for (int i = 0; i < 26; i++)
                {
                    Console.WriteLine(ceasarDecryptor.Decryptor(text, i));
                }
            }
            Console.ReadKey();
        }
    }
}
