package gash.router.server.raft;

//import gash.router.server.*;
//import server.ServerUtils;

import java.util.Random;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
//import raft.proto.AppendEntriesRPC.AppendEntries.RequestType;
import raft.proto.Vote.ResponseVote;
import raft.proto.Work.WorkMessage;
import gash.router.server.raft.TimerRoutine;
import io.netty.channel.ChannelFuture;

public class Follower extends Service implements Runnable {

	public static boolean HBrecvd = false;
	NodeTimer timer;
	protected static Logger logger = (Logger) LoggerFactory.getLogger("Follower");
	Thread followerThread = null;
	private static Follower INSTANCE = null;
	TimerRoutine getTimer;
	public static boolean voted = false;
	public static int lastVotedTerm = 0;

	public static Follower getInstance() {
		if (INSTANCE == null) {
			INSTANCE = new Follower();

		}
		return INSTANCE;
	}

	@Override
	
	public void run() {
		logger.info("Follower started");
		initFollower();

		followerThread = new Thread(){
		    public void run(){
				while (running ) {
					while (NodeState.getInstance().getState() == NodeState.FOLLOWER) {
					}
				}

		    }
		 };

		followerThread.start();
//		ServerQueueService.getInstance().createGetQueue();
	}
	
	private void initFollower() {
		// TODO Auto-generated method stub

		if(NodeState.currentTerm > lastVotedTerm)
			voted=false;
		
		timer = new NodeTimer();

		timer.schedule(new Runnable() {
			@Override
			public void run() {
				NodeState.getInstance().setState(NodeState.CANDIDATE);
			}
		}, getTimer. getElectionTimeout());

	}
	
	
	
	public void onReceivingHeartBeatPacket() {
		System.out.println("Heartbeat recieved");
		timer.reschedule(getTimer.getElectionTimeout());
	}
	
	@Override
	public WorkMessage handleRequestVote(WorkMessage workMessage) {

		if (workMessage.getVoteRPCPacket().getRequestVote().getTimeStampOnLatestUpdate() < NodeState.getTimeStampOnLatestUpdate()) {
//			logger.info((NodeState.getInstance().getServerState().getConf().getNodeId()) + " has replied NO");
			return MessageBuilder.prepareResponseVote(ResponseVote.IsVoteGranted.NO);

		}
//		Logger.DEBUG(NodeState.getInstance().getServerState().getConf().getNodeId() + " has replied YES");
		if (workMessage.getVoteRPCPacket().getResponseVote().getTerm() >= NodeState.currentTerm && voted) {
			lastVotedTerm = NodeState.currentTerm;
			voted = true;
			return MessageBuilder.prepareResponseVote(ResponseVote.IsVoteGranted.YES);
		}
		else
			return MessageBuilder.prepareResponseVote(ResponseVote.IsVoteGranted.NO);


	}
	
	@Override
	public void handleHeartBeat(WorkMessage wm) {
//		Logger.DEBUG("HeartbeatPacket received from leader :" + wm.getHeartBeatPacket().getHeartbeat().getLeaderId());
		NodeState.currentTerm = wm.getHeartBeatPacket().getHeartbeat().getTerm();
		onReceivingHeartBeatPacket();
		logger.info("Heartbeat recieved");

//		WorkMessage heartBeatResponse = MessageBuilder.prepareHeartBeatResponse();
//
//		for (EdgeInfo ei : NodeState.getInstance().getServerState().getEmon().getOutboundEdges().getMap().values()) {
//
//			if (ei.isActive() && ei.getChannel() != null
//					&& ei.getRef() == wm.getHeartBeatPacket().getHeartbeat().getLeaderId()) {
//
//				Logger.DEBUG("Sent HeartBeatResponse to " + ei.getRef());
//				ChannelFuture cf = ei.getChannel().writeAndFlush(heartBeatResponse);
//				if (cf.isDone() && !cf.isSuccess()) {
//					Logger.DEBUG("failed to send message (HeartBeatResponse) to server");
//				}
//			}
//		}

	}
	
//	@Override
//	public void handleAppendEntries(WorkMessage wm) {
//		String key = wm.getAppendEntriesPacket().getAppendEntries().getImageMsg().getKey();
//		byte[] image = wm.getAppendEntriesPacket().getAppendEntries().getImageMsg().getImageData().toByteArray();
//		long unixTimeStamp = wm.getAppendEntriesPacket().getAppendEntries().getTimeStampOnLatestUpdate();
//		RequestType type = wm.getAppendEntriesPacket().getAppendEntries().getRequestType();
		
//		if (type == RequestType.GET) {
//			DatabaseService.getInstance().getDb().get(key);
//		} else if (type == RequestType.POST) {
//			NodeState.getTimeStampOnLatestUpdate();
//			DatabaseService.getInstance().getDb().post(key, image, unixTimeStamp);
//		} else if (type == RequestType.PUT) {
//			NodeState.setTimeStampOnLatestUpdate(unixTimeStamp);
//			DatabaseService.getInstance().getDb().put(key, image, unixTimeStamp);
//		} else if (type == RequestType.DELETE) {
//			NodeState.setTimeStampOnLatestUpdate(System.currentTimeMillis());
//			DatabaseService.getInstance().getDb().delete(key);
//		}
//		
//		Logger.DEBUG("Inserted entry with key " + key + " received from "
//				+ wm.getAppendEntriesPacket().getAppendEntries().getLeaderId());
//	}


	@Override
	public void startService(Service service) {

		running = Boolean.TRUE;
		cthread = new Thread((Follower) service);
		cthread.start();

	}

	@Override
	public void stopService() {
		running = Boolean.FALSE;
	}


}
