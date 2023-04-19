#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: toa
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
from gnuradio import zeromq



from gnuradio import qtgui

class pager(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pager")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.rtl_samp_rate = rtl_samp_rate = 264600
        self.decimation = decimation = 12
        self.samp_rate = samp_rate = rtl_samp_rate // decimation
        self.lpf = lpf = firdes.low_pass(1.0, rtl_samp_rate, rtl_samp_rate / (2*decimation),5000, window.WIN_HAMMING, 6.76)
        self.hw_freq = hw_freq = 157.95e6

        ##################################################
        # Blocks
        ##################################################

        self.zeromq_pub_sink_0_0 = zeromq.pub_sink(gr.sizeof_short, 1, 'ipc:///tmp/pager_ch2.socket', 500, False, (-1), '', False)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_short, 1, 'ipc:///tmp/pager_ch1.socket', 500, False, (-1), '', False)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
            2048, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'CH2', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(False)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-80, -10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.qwidget(), Qt.QWidget)

        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            2048, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'CH1', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(False)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-80, -10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            4096, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            rtl_samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-100), 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(False)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)

        self.qtgui_freq_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32('ip:pluto.local' if 'ip:pluto.local' else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(int(hw_freq))
        self.iio_pluto_source_0.set_samplerate(rtl_samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'slow_attack')
        self.iio_pluto_source_0.set_gain(0, 64)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(decimation, lpf, (157.925e6 - hw_freq), rtl_samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation, lpf, (157.95e6 - hw_freq), rtl_samp_rate)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 8192)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 8192)
        self.analog_nbfm_rx_0_0_0_0 = analog.nbfm_rx(
        	audio_rate=samp_rate,
        	quad_rate=samp_rate,
        	tau=(50e-6),
        	max_dev=5e3,
          )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=samp_rate,
        	quad_rate=samp_rate,
        	tau=(50e-6),
        	max_dev=5e3,
          )
        self.analog_agc_xx_0_0 = analog.agc_ff((1e-4), 0.2, 0.2)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_ff((1e-4), 0.2, 0.2)
        self.analog_agc_xx_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.blocks_float_to_short_0_0, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.analog_nbfm_rx_0_0_0_0, 0), (self.analog_agc_xx_0_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.zeromq_pub_sink_0, 0))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.zeromq_pub_sink_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_nbfm_rx_0_0_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pager")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_rtl_samp_rate(self):
        return self.rtl_samp_rate

    def set_rtl_samp_rate(self, rtl_samp_rate):
        self.rtl_samp_rate = rtl_samp_rate
        self.set_lpf(firdes.low_pass(1.0, self.rtl_samp_rate, self.rtl_samp_rate / (2*self.decimation), 5000, window.WIN_HAMMING, 6.76))
        self.set_samp_rate(self.rtl_samp_rate // self.decimation)
        self.iio_pluto_source_0.set_samplerate(self.rtl_samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.rtl_samp_rate)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.set_lpf(firdes.low_pass(1.0, self.rtl_samp_rate, self.rtl_samp_rate / (2*self.decimation), 5000, window.WIN_HAMMING, 6.76))
        self.set_samp_rate(self.rtl_samp_rate // self.decimation)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_lpf(self):
        return self.lpf

    def set_lpf(self, lpf):
        self.lpf = lpf
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.lpf)
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(self.lpf)

    def get_hw_freq(self):
        return self.hw_freq

    def set_hw_freq(self, hw_freq):
        self.hw_freq = hw_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq((157.95e6 - self.hw_freq))
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq((157.925e6 - self.hw_freq))
        self.iio_pluto_source_0.set_frequency(int(self.hw_freq))




def main(top_block_cls=pager, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
