using BlockchainEx.Core.Models;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace BlockchainEx.Core.Services
{
    public interface IBlockchainService
    {
       /* public Block CreateGenesisBlock();
        public void AddGenesisBlock();
        public Block GetLatestBlock();*/
        public void AddBlock(Block block);
        public List<Block> GetBlock();
    }
}
