using Ceasar.API;
using Ceasar.Model;
using Refit;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ceasar.Services
{
    public class TextService:ITextService
    {
       // public List<Text> texts = new List<Text>();
        ITextAPI textAPI;

        public async Task<List<Text>> GetTexts()
        {
            textAPI = RestService.For<ITextAPI>("https://api.jsonbin.io/");
            return await textAPI.DownloadText();
        }
    }
}
