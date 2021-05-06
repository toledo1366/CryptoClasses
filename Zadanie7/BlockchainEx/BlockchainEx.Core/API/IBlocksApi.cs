using BlockchainEx.Core.Models;
using Refit;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace BlockchainEx.Core.API
{
    interface IBlocksApi
    {
        [Get("/b/60943f0e4f94d769b1dc81e2")]
        List<Block> GetBlocks();
    }
}
