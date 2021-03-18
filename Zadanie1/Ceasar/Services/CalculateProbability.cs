using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ceasar.Services
{
    public class CalculateProbability
    {
        double[] englishLettersProbabilities = {0.073, 0.009, 0.030, 0.044, 0.130, 0.028, 0.016, 0.035, 0.074,
                0.002, 0.003, 0.035, 0.025, 0.078, 0.074, 0.027, 0.003,
                0.077, 0.063, 0.093, 0.027, 0.013, 0.016, 0.005, 0.019, 0.001};
        char[] englishAlphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
                ,'u','v','w','x','y','z' };

        public double CalcProbability(string text)
        {
            double probability = 0;
            for (int i = 0; i < text.Length; i++)
            {
                probability += englishLettersProbabilities[Array.IndexOf(englishAlphabet, text[i])];
            }
            return probability;
        }
    }
}
