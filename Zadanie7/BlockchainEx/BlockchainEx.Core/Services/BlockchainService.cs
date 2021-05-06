using BlockchainEx.Core.API;
using BlockchainEx.Core.Models;
using Refit;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace BlockchainEx.Core.Services
{
    public class BlockchainService : IBlockchainService
    {
        public List<Block> Chain = new List<Block>();
        IBlocksApi blocksApi;

        public BlockchainService()
        {
            blocksApi = RestService.For<IBlocksApi>("https://api.jsonbin.io");
        }

        public void AddBlock(Block block)   //Function to add new block
        {
            Block latestBlock = Chain[Chain.Count - 1];
            block.Index = latestBlock.Index + 1;
            block.PreviousHash = latestBlock.Hash;
            block.Hash = block.CalculateHash();
            Chain.Add(block);
        }

        public List<Block> GetBlock()
        {
            Chain = blocksApi.GetBlocks();
            return Chain;
        }
    }
}
