using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Refit;
using Ceasar.Model;

namespace Ceasar.API
{
    public interface ITextAPI
    {
        [Get("/b/60427817b3238f032ca4ccf2/1")]
        Task<List<Text>> DownloadText();
    }
}
