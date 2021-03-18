using Ceasar.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ceasar.Services
{
    public class CeasarDecryptor
    {
        List<string> textToDecrypt = new List<string>();

        public List<string> GetTexts(List<Text> texts)
        {
            foreach (Text text in texts)
            {
                this.textToDecrypt.Add(text.DecryptedText.ToLower());
            }
            return textToDecrypt;
        }

        public string Decryptor(string text, int jump)
        {
            int ascii;
            string decryptedText = "";
            text = text.ToLower();
            for(int i = 0; i<text.Length; i++)
            {
                ascii = Convert.ToInt32(text[i]) + jump;
                if(ascii>=97 && ascii <= 122)
                {
                    decryptedText += Convert.ToChar(ascii);
                }
                else if (ascii > 122)
                {
                    ascii = (ascii - 122) + 96;
                    decryptedText += Convert.ToChar(ascii);
                }
                else if(ascii < 97)
                {
                    ascii = 123 - (97 - ascii);
                    decryptedText += Convert.ToChar(ascii);
                }
            }
            return decryptedText;
        }

        public void ShowMostProbablyDecodedText(string decodedText)
        {
            CalculateProbability calculate = new CalculateProbability();
            double[] values = new double[26];
            for(int i = 0; i < values.Length; i++)
            {
                values[i] = calculate.CalcProbability(decodedText);
            }
            int index = Array.IndexOf(values, values.Max());
            Console.WriteLine("Word was decoded as {0} with value {1}",decodedText,values.Max());
        }
    }
}
