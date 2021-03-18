using Ceasar.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ceasar.Services
{
    public interface ITextService
    {
        Task<List<Text>> GetTexts();
    }
}
